from rest_framework.views import APIView
from core.permissions import IsTeacher,IsStudent
from core.helpers import api_response
from student.serializers.student_test_serializer import StudentTestGetSerializer,StudentResultGetSerializer
from teacher.models.teacher_test_model import Test
from student.models.student_test_model import StudentTest
from student.models.student_test_result import TestResult
from teacher.models.teachers import Teacher



class StudentGetTestdetailView(APIView):
    permission_classes = (IsStudent,)

    def post(self,request):
        user_id = request.user.id
        course_id = request.data.get("id", None)
        # teacher_id = Teacher.objects.get(teacher_id = user_id).id
        tests = Test.objects.filter(course_id=course_id,active=True)
        if tests:
            serialized_test = StudentTestGetSerializer(tests, context={"user_id":request.user.id},many = True)
            return api_response(200,"Test retrived successfully", serialized_test.data, status=True)
        else:
            return api_response(200, "No Test found", [], status=True)






class ActiveStudentTestView(APIView):
    """
                 student can active the Studenttest.
    """
    permission_classes = (IsStudent,)

    def put(self, request):
        test_id = request.data.get("test_id",None)
        course_id = request.data.get("course_id",None)
        userid = request.user.id
        try:
            student_test = StudentTest.objects.get(test_id=test_id,course_id=course_id,student_id=userid)
            if student_test.test_attempt == False:
                student_test.test_attempt =True
                student_test.save()
                return api_response(200, "Student already given the test", request.data, status=True)
            elif student_test.test_attempt == True:
                # student_test.test_attempt = False
                # student_test.save()
                return api_response(200, "Student already given the test", request.data, status=True)

        except StudentTest.DoesNotExist:
            return api_response(200, "Test Not Found", [], status=True)



class StudentTestResultView(APIView):
    permission_classes = (IsStudent,)

    def post(self,request):
        try:
            test_id = request.data.get("id", None)
            userid = request.user.id
            obj = StudentTest.objects.get(student_id=userid,test_id=int(test_id))
            test =Test.objects.get(id=test_id)
            total_mark = test.total_marks
            is_correct = len(list(filter(lambda ans:ans["is_correct"]== True,obj.question)))
            is_attempt = len(list(filter(lambda ans: ans["is_attempt"] == True, obj.question)))
            no_of_skip = len(list(filter(lambda ans: ans["is_attempt"] == False, obj.question)))
            # data =[]
            # data2={}
            data1 ={"total_mark": total_mark, "score": is_correct , "no_of_attempt": is_attempt, "no_of_skip": no_of_skip}
            print(data1)
            try:
                student_test = TestResult.objects.get(test=test_id,student=userid)
            except:
                student_test = TestResult.objects.create(
                    test_id=test_id,
                    student_id=request.user.id,
                    total_mark=total_mark,
                    score=is_correct,
                    no_of_skip=no_of_skip,
                    no_of_attempt=is_attempt
                )
            serializer = StudentResultGetSerializer(obj)
            data = serializer.data
            data.update(data1)
            return api_response(200, "Result retrived successfully", [data], status=True)
        except StudentTest.DoesNotExist:
            return api_response(200, "Test Not Found", [], status=True)












# class StudentTestView(APIView):
#     permission_classes = (IsStudent,)
#
#     def post(self,request):
#         user_id = request.user.id
#         # request.POST._mutable = True
#         serialized_test = StudentTestPostSerializer(data = request.data)
#         if serialized_test.is_valid(raise_exception=True):
#             serialized_test.save(student_id=request.user.id)
#             return api_response(200,"Student Test created  successfully",serialized_test.data, status=True)
#         return api_response(400,"Student Test failed",{}, status=False)
