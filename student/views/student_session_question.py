from rest_framework.permissions import IsAuthenticated
import pytz
from rest_framework.views import APIView
from django.utils import timezone
from core.permissions import IsStudent
from core.helpers import api_response
from student.models.course_booking import CourseBooking
from counsellor.models.counsellor_test_model import CounsellorTest
from counsellor.models.counsellor_question_model import CounsellorQuestion
from student.models.student_session_test import StudentSessionTest
# from teacher.serializers.teacher_question_serializer import QuestionGetSerializer
from counsellor.serializers.counsellor_question_serializer import CounsellorQuestionGetSerializer
from student.serializers.student_sessiontest_serializer import StudentAnswerSerializer


# booking_course = CourseBooking.objects.filter(user_id=request.user.id, is_booking=True)
# # course_list =[]
# for cors in booking_course:

class StudentSessionQuestionView(APIView):
    permission_classes = (IsStudent,)

    def post(self,request):
        try:
            test_id = request.data.get("id", None)
            tests =  CounsellorTest.objects.filter(id=test_id)
            for obj in tests:
                question = CounsellorQuestion.objects.filter(test_id=test_id)
                if question:
                    serializer = CounsellorQuestionGetSerializer(question, many=True)
                    qsns = []
                    for item in serializer.data:
                        item.update({"is_attempt":False,"is_correct":False,"stu_ans":None})
                        qsns.append(item)
                        # print(qsns)
                    try:
                        student_test = StudentSessionTest.objects.get(test=test_id)
                    except:
                        student_test = StudentSessionTest.objects.create(
                            test_id =test_id,
                            student_id=request.user.id,
                            session_id=obj.session_id,
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





class StudentSessionTestAnswerView(APIView):
    permission_classes = (IsStudent,)

    def put(self,request):
        question_id = request.data.get("id", None)
        test_id = request.data.get("test_id", None)
        stu_ans = request.data.get("answer", None)
        qus_attempt = request.data.get("is_attempt", None)
        qus_correct = request.data.get("is_correct", None)
        userid = request.user.id
        try:
            obj = StudentSessionTest.objects.get(student_id=userid,test_id=test_id)
            serializer = StudentAnswerSerializer(obj)
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

        except StudentSessionTest.DoesNotExist:
            return api_response(404, "Student doesnot exits", {}, status=False)

        except IndexError:
            return api_response(404, "invalid question id", {}, status=False)



