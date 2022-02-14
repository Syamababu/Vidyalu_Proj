from rest_framework.views import APIView
from core.permissions import IsTeacher,IsStudent
from core.helpers import api_response
from counsellor.models.counsellor_test_model import CounsellorTest
from student.serializers.student_sessiontest_serializer import StudentSessionTestSerializer,StudentSessionResultGetSerializer
from student.models.student_session_test import StudentSessionTest
from student.models.student_sessiontest_result import SessionTestResult
from teacher.models.teachers import Teacher



class StudentSessionTestdetailView(APIView):
    permission_classes = (IsStudent,)

    def post(self,request):
        user_id = request.user.id
        session_id = request.data.get("id", None)
        # teacher_id = Teacher.objects.get(teacher_id = user_id).id
        tests = CounsellorTest.objects.filter(session_id=session_id,active=True)
        if tests:
            serialized_test = StudentSessionTestSerializer(tests, context={"user_id":request.user.id},many = True)
            return api_response(200,"SessionTest retrived successfully", serialized_test.data, status=True)
        else:
            return api_response(200, "No Test found", [], status=True)






class ActiveStudentSessionTestView(APIView):
    """
                 student can active the Studenttest.
    """
    permission_classes = (IsStudent,)

    def put(self, request):
        test_id = request.data.get("test_id",None)
        session_id = request.data.get("session_id",None)
        userid = request.user.id
        try:
            student_test = StudentSessionTest.objects.get(test_id=test_id,session_id=session_id,student_id=userid)
            if student_test.test_attempt == False:
                student_test.test_attempt =True
                student_test.save()
                return api_response(200, "Student already given the test", request.data, status=True)
            elif student_test.test_attempt == True:
                # student_test.test_attempt = False
                # student_test.save()
                return api_response(200, "Student already given the test", request.data, status=True)

        except StudentSessionTest.DoesNotExist:
            return api_response(200, "Test Not Found", [], status=True)



class StudentSessionTestResultView(APIView):
    permission_classes = (IsStudent,)

    def post(self,request):
        try:
            test_id = request.data.get("id", None)
            userid = request.user.id
            obj = StudentSessionTest.objects.get(student_id=userid,test_id=int(test_id))
            test =CounsellorTest.objects.get(id=test_id)
            mark = test.total_marks
            correct = len(list(filter(lambda ans:ans["is_correct"]== True,obj.question)))
            attempt = len(list(filter(lambda ans: ans["is_attempt"] == True, obj.question)))
            skip = len(list(filter(lambda ans: ans["is_attempt"] == False, obj.question)))
            # data1 ={"total_mark": mark, "score": correct , "no_of_attempt": attempt, "no_of_skip": skip}
            # print(data1)
            try:
                student_test = SessionTestResult.objects.get(test=test_id,student=userid)
            except:
                print("total_mark",mark)
                print(type(mark))
                print(type(test_id))
                print(type(userid))
                student_test = SessionTestResult.objects.create(
                    test_id=test_id,
                    student_id=request.user.id,
                    total_mark=mark,
                    score=correct,
                    no_of_skip=skip,
                    no_of_attempt=attempt
                )
                # student_test.save()
            serializer = StudentSessionResultGetSerializer(student_test)
            # data = serializer.data
            # data.update(data1)
            return api_response(200, "Result retrived successfully", [serializer.data], status=True)
        except StudentSessionTest.DoesNotExist:
            return api_response(200, "Test Not Found", [], status=True)




# class StudentTestResultdetailView(APIView):
#     permission_classes = (IsStudent,)
#
#     def get(self,request):
#         user_id = request.user.id
#         tests = Test.objects.filter(course_id=course_id,active=True)
#         if tests:
#             serialized_test = StudentTestGetSerializer(tests, context={"user_id":request.user.id},many = True)
#             return api_response(200,"Test retrived successfully", serialized_test.data, status=True)
#         else:
#             return api_response(200, "No Test found", [], status=True)








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
