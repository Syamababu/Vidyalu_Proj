
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from core.permissions import IsCounsellor
from core.helpers import api_response

from counsellor.serializers.counsellor_test_serializer import CounsellorTestGetSerializer,CounsellorTestPostSerializer,SessionResultStudentSerializer
from counsellor.models.counsellor_test_model import CounsellorTest
from counsellor.models.counsellors import Counsellor
from student.models.student_sessiontest_result import SessionTestResult

class CounsellorCreatTestView(APIView):
    permission_classes = (IsCounsellor,)

    def post(self,request):
        user_id = request.user.id
        # teacher_id = Teacher.objects.get(teacher_id = user_id).id
        # request.data._mutable = True
        # request.data['teacher'] = teacher_id
        # request.data._mutable = False
        # print(request.data)

        request.POST._mutable = True
        serialized_test = CounsellorTestPostSerializer(data = request.data)
        if serialized_test.is_valid(raise_exception=True):
            serialized_test.save(counsellor_id=request.user.id)
            return api_response(200,"Counsellor Test uploaded successfully",serialized_test.data, status=True)
        return api_response(400,"Counsellor Test upload failed",{}, status=False)


class CounsellorGetTestView(APIView):
    permission_classes = (IsCounsellor,)

    def post(self,request):
        user_id = request.user.id
        session_id = request.data.get("id", None)
        # teacher_id = Teacher.objects.get(teacher_id = user_id).id
        tests = CounsellorTest.objects.filter(counsellor_id = user_id,session_id=session_id)
        if tests:
            serialized_test = CounsellorTestGetSerializer(tests, many = True)
            return api_response(200,"Counsellor Test retrived successfully", serialized_test.data, status=True)
        else:
            return api_response(200, "No Test found", [], status=True)



class CounsellorPutTestView(APIView):
    permission_classes = (IsCounsellor,)

    def put(self,request):
        request.POST._mutable = True
        user_id = request.user.id
        counsellor_id = Counsellor.objects.get(counsellor_id = user_id).id
        test_id = request.data.get("id", None)
        test = CounsellorTest.objects.get(id=test_id)
        serialized_test = CounsellorTestPostSerializer(test,data=request.data,partial=True)
        if serialized_test.is_valid(raise_exception=True):
            serialized_test.save(counsellor_id=request.user.id)
            return api_response(200,"Test updated successfully",serialized_test.data, status=True)
        return api_response(400,"Test update failed",{}, status=False)


class ActiveSessionTestView(APIView):
    """
                 teacher can active and inactive the test.
    """
    permission_classes = (IsCounsellor,)

    def put(self, request):
        try:
            test_id = request.data.get("id",None)
            test = CounsellorTest.objects.get(id=test_id)
            if test.active == False:
                test.active =True
                test.save()
                return api_response(200, "Test will be Activate successfully", request.data, status=True)
            elif test.active == True:
                test.active = False
                test.save()
                return api_response(200, "Test will be Deactivate successfully", request.data, status=True)

        except CounsellorTest.DoesNotExist:
            return api_response(400, "Test Not Found", {}, status=False)


class CounsellorGetStudentDetailView(APIView):
    permission_classes = (IsCounsellor,)

    def post(self, request):
        # user_id = request.user.id
        # course_id = request.data.get("id", None)
        try:
            test_id = request.data.get("id", None)
            # teacher_id = Teacher.objects.get(teacher_id = user_id).id
            print("1")
            tests = SessionTestResult.objects.filter(test_id=test_id)
            print(tests)
            if tests:
                serialized_test = SessionResultStudentSerializer(tests, many=True)
                return api_response(200, "Student details retrived successfully", serialized_test.data, status=True)
            else:
                return api_response(200, "No Student details found", [], status=True)

        except SessionTestResult.DoesNotExist:
            return api_response(400, "Test Not Found", {}, status=False)



class CounsellorGetStudentTestResultView(APIView):
    permission_classes = (IsCounsellor,)

    def post(self, request):
        # user_id = request.user.id
        # course_id = request.data.get("id", None)
        try:
            stu_id = request.data.get("id", None)
            # teacher_id = Teacher.objects.get(teacher_id = user_id).id
            print("1")
            tests = SessionTestResult.objects.get(student_id=stu_id)
            print(tests)
            if tests:
                serialized_test = SessionResultStudentSerializer(tests)
                return api_response(200, "Student TestResult retrived successfully", serialized_test.data, status=True)
            else:
                return api_response(200, "No Student TestResult found", [], status=True)
        except SessionTestResult.DoesNotExist:
            return api_response(400, "Student Not Found", {}, status=False)

    # def delete(self,request,pk):
    #     try:
    #         test = Test.objects.get(pk = pk)
    #         test.delete()
    #         return api_response(200,"Test deleted successfully",{}, status=True)
    #     except:
    #         return api_response(400,"Test delete failed",{}, status = False)
