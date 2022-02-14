from rest_framework.permissions import IsAuthenticated
import pytz
from rest_framework.views import APIView
from django.utils import timezone
from core.permissions import IsStudent
from core.helpers import api_response
from student.models.course_booking import CourseBooking
from teacher.models.teacher_test_model import Test
from teacher.models.teacher_question_model import Question
from student.models.student_test_model import StudentTest
from teacher.serializers.teacher_question_serializer import QuestionGetSerializer
from student.serializers.student_test_serializer import StudentTestGetSerializer


# booking_course = CourseBooking.objects.filter(user_id=request.user.id, is_booking=True)
# # course_list =[]
# for cors in booking_course:

class StudentQuestionView(APIView):
    permission_classes = (IsStudent,)

    def post(self,request):
        try:
            test_id = request.data.get("id", None)
            tests =  Test.objects.filter(id=test_id)
            for obj in tests:
                question = Question.objects.filter(test_id=test_id)
                if question:
                    serializer = QuestionGetSerializer(question, many=True)
                    qsns = []
                    for item in serializer.data:
                        item.update({"is_attempt":False,"is_correct":False,"stu_ans":None})
                        qsns.append(item)
                        # print(qsns)
                    try:
                        student_test = StudentTest.objects.get(test=test_id)
                    except:
                        student_test = StudentTest.objects.create(
                            test_id =test_id,
                            student_id=request.user.id,
                            course_id=obj.course_id,
                            question=qsns
                        )
                    return api_response(200, "Question retrived successfully", qsns, status=True)
                else:
                    return api_response(200, "No Question found", [], status=True)
            return api_response(400, "Test id Not Found", {}, status=False)
        except :
            return api_response(400, "Test Not Found", {}, status=False)



# def validate_answer(qtn,stu_ans):
#     for item in qtn["option"]:
#         if item["correct"]:
#             if item["option"]==stu_ans:
#                 return True
#     return False





class StudentTestView(APIView):
    permission_classes = (IsStudent,)

    def put(self,request):
        question_id = request.data.get("id", None)
        test_id = request.data.get("test_id", None)
        stu_ans = request.data.get("answer", None)
        qus_attempt = request.data.get("is_attempt", None)
        qus_correct = request.data.get("is_correct", None)
        userid = request.user.id
        try:
            obj = StudentTest.objects.get(student_id=userid,test_id=test_id)
            serializer = StudentTestGetSerializer(obj)
            qtn=list(filter(lambda quns: quns['id'] == int(question_id), obj.question))[0]
            i=obj.question.index(qtn)
            qtn['is_attempt']=qus_attempt
            qtn.update({'is_attempt': qus_attempt})
            qtn["stu_ans"]=stu_ans
            qtn.update({'stu_ans': stu_ans})
            qtn["is_correct"]=qus_correct
            qtn.update({'is_correct': qus_correct})
            (obj.question[i]).update(qtn)
            obj.save()
            return api_response(200, "Student answer Updated successfully", [qtn], status=True)

        except StudentTest.DoesNotExist:
            return api_response(404, "Student doesnot exits", {}, status=False)

        # except IndexError:
        #     return api_response(404, "invalid question id", {}, status=False)



