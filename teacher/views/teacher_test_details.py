
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from core.permissions import IsTeacher
from core.helpers import api_response

from teacher.serializers.teacher_test_Serializer import TestGetSerializer,TestPostSerializer,TestStudentGetSerializer
from teacher.models.teacher_test_model import Test
from teacher.models.teachers import Teacher
from student.models.student_test_result import TestResult

class TeacherCreatTestView(APIView):
    permission_classes = (IsTeacher,)

    def post(self,request):
        user_id = request.user.id
        # teacher_id = Teacher.objects.get(teacher_id = user_id).id
        # request.data._mutable = True
        # request.data['teacher'] = teacher_id
        # request.data._mutable = False
        # print(request.data)

        request.POST._mutable = True
        serialized_test = TestPostSerializer(data = request.data)
        if serialized_test.is_valid(raise_exception=True):
            serialized_test.save(teacher_id=request.user.id)
            return api_response(200,"Test uploaded successfully",serialized_test.data, status=True)
        return api_response(400,"Test upload failed",{}, status=False)


class TeacherGetTestView(APIView):
    permission_classes = (IsTeacher,)

    def post(self,request):
        user_id = request.user.id
        course_id = request.data.get("id", None)
        # teacher_id = Teacher.objects.get(teacher_id = user_id).id
        tests = Test.objects.filter(teacher_id = user_id,course_id=course_id)
        if tests:
            serialized_test = TestGetSerializer(tests, many = True)
            return api_response(200,"Test retrived successfully", serialized_test.data, status=True)
        else:
            return api_response(200, "No Test found", [], status=True)



class TeacherPutTestView(APIView):
    permission_classes = (IsTeacher,)

    def put(self,request):
        request.POST._mutable = True
        print("request.data",request.data)
        user_id = request.user.id
        teacher_id = Teacher.objects.get(teacher_id = user_id).id
        test_id = request.data.get("id", None)
        test = Test.objects.get(id=test_id)
        serialized_test = TestPostSerializer(test,data=request.data,partial = True)
        if serialized_test.is_valid(raise_exception=True):
            serialized_test.save(teacher_id=request.user.id)
            return api_response(200,"Test updated successfully",serialized_test.data, status=True)
        return api_response(400,"Test update failed",{}, status=False)


class ActiveTestView(APIView):
    """
                 teacher can active and inactive the test.
    """
    permission_classes = (IsTeacher,)

    def put(self, request):
        try:
            test_id = request.data.get("id",None)
            test = Test.objects.get(id=test_id)
            if test.active == False:
                test.active =True
                test.save()
                return api_response(200, "Test will be Activate successfully", request.data, status=True)
            elif test.active == True:
                test.active = False
                test.save()
                return api_response(200, "Test will be Deactivate successfully", request.data, status=True)

        except Test.DoesNotExist:
            return api_response(400, "Test Not Found", {}, status=False)


class TeacherGetStudentDetailView(APIView):
    permission_classes = (IsTeacher,)

    def post(self, request):
        # user_id = request.user.id
        # course_id = request.data.get("id", None)
        try:
            test_id = request.data.get("id", None)
            # teacher_id = Teacher.objects.get(teacher_id = user_id).id
            print("1")
            tests = TestResult.objects.filter(test_id=test_id)
            print(tests)
            if tests:
                serialized_test = TestStudentGetSerializer(tests, many=True)
                return api_response(200, "Student details retrived successfully", serialized_test.data, status=True)
            else:
                return api_response(200, "No Student details found", [], status=True)
        except TestResult.DoesNotExist:
            return api_response(400, "Test Not Found", {}, status=False)


class TeacherGetStudentTestResultView(APIView):
    permission_classes = (IsTeacher,)

    def post(self, request):
        # user_id = request.user.id
        # course_id = request.data.get("id", None)
        try:
            stu_id = request.data.get("id", None)
            # teacher_id = Teacher.objects.get(teacher_id = user_id).id
            print("1")
            tests = TestResult.objects.get(student_id=stu_id)
            print(tests)
            if tests:
                serialized_test = TestStudentGetSerializer(tests)
                return api_response(200, "Student TestResult retrived successfully", serialized_test.data, status=True)
            else:
                return api_response(200, "No Student TestResult found", [], status=True)
        except TestResult.DoesNotExist:
            return api_response(400, "Test Not Found", {}, status=False)



    # def delete(self,request,pk):
    #     try:
    #         test = Test.objects.get(pk = pk)
    #         test.delete()
    #         return api_response(200,"Test deleted successfully",{}, status=True)
    #     except:
    #         return api_response(400,"Test delete failed",{}, status = False)
