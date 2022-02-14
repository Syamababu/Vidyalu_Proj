from rest_framework.views import APIView
from core.permissions import IsStudent
from core.helpers import api_response
from student.serializers.course_report_serializer import CourseReportSerializer,CourseReportGetSerializer
from student.models.student_course_report import CourseReport




class StudentCourseReportView(APIView):
    """
        student can report the course.
    """
    permission_classes = (IsStudent,)

    def post(self, request):
            user = request.user.id
            serializer = CourseReportSerializer(data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save(user_id=user)
                return api_response(200, "Course report successfully", serializer.data, status=True)
            else:
                return api_response(400, "Course report failed", {}, status=False)





class StudentCourseReportGetView(APIView):
    permission_classes = (IsStudent,)

    def post(self,request):
        user = request.user.id
        course_id = request.data.get("id", None)
        report = CourseReport.objects.filter(course_id=course_id)
        print(report)
        if report:
            serialized_report = CourseReportGetSerializer(report,many=True)
            return api_response(200,"Course report retrived successfully", serialized_report.data, status=True)
        else:
            return api_response(200, "No Course report found", [], status=True)



class StudentCourseReportEditView(APIView):
    """
           student can update report the course.
    """
    permission_classes = (IsStudent,)

    def put(self, request):
        try:
            user = request.user.id
            course_id = request.data.get("course", None)
            course = CourseReport.objects.get(user_id=user,course_id=course_id)
            serializer = CourseReportSerializer(course, data=request.data, partial=True)
            if serializer.is_valid(raise_exception=True):
                serializer.save(user_id=user)
                return api_response(200, "Course report Updated successfully", serializer.data, status=True)
            else:
                return api_response(400, "Invalid data", {}, status=False)
        except CourseReport.DoesNotExist:
            return api_response(400, "Course Not Found", {},status=False)


