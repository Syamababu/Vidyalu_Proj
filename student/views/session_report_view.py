from rest_framework.views import APIView
from core.permissions import IsStudent
from core.helpers import api_response
from student.serializers.session_report_serializer import SessionReportSerializer,SessionReportGetSerializer
from student.models.student_session_report import SessionReport
from rest_framework.permissions import IsAuthenticated


class StudentSessionReportView(APIView):
    """
        student can report the session .
    """
    permission_classes = (IsStudent,)


    def post(self, request):
            user = request.user.id
            serializer = SessionReportSerializer(data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save(user_id=user)
                return api_response(200, "Session report successfully", serializer.data, status=True)
            else:
                return api_response(400, "Session report failed", {}, status=False)





class StudentSessionReportGetView(APIView):
    permission_classes = (IsStudent,)

    def post(self,request):
        user = request.user.id
        # teacher_id = Teacher.objects.get(teacher_id = user_id).id
        session_id = request.data.get("id", None)
        report = SessionReport.objects.filter(session_id=session_id)
        if report:
            serialized_rating = SessionReportGetSerializer(report,many=True)
            return api_response(200,"Session report retrived successfully", serialized_rating.data, status=True)
        else:
            return api_response(200, "No Session report found", [], status=True)


class StudentSessionReportEditView(APIView):
    """
            student can update report the session .
    """
    permission_classes = (IsStudent,)

    def put(self, request):
        try:
            user = request.user.id
            session_id = request.data.get("session", None)
            session = SessionReport.objects.get(user_id=user,session_id=session_id)
            serializer = SessionReportSerializer(session, data=request.data, partial=True)
            if serializer.is_valid(raise_exception=True):
                serializer.save(user_id=user)
                return api_response(200, "Session report Updated successfully", serializer.data, status=True)
            else:
                return api_response(400, "Invalid data", {}, status=False)
        except SessionReport.DoesNotExist:
            return api_response(400, "Session Not Found", {},status=False)
