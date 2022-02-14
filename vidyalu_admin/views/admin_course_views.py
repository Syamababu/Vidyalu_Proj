from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from core.helpers import api_response
from teacher.models.courses_model import Course
from vidyalu_admin.serializers.admin_course_serializer import CourseDetailSerializer,AdminCourseBookingSerializer,AdminCourseReportGetSerializer
from student.models.course_booking import CourseBooking
from student.models.student_course_report import CourseReport

class AdminCourseDetailsView(APIView):
    """
        Admin can view all the course details.
    """
    permission_classes = (IsAdminUser,)

    def get(self, request):
        course = Course.objects.all().order_by('-created_at')
        if course:
            serializer = CourseDetailSerializer(course, many=True)
            return api_response(200, "Course retrieved successfully.", serializer.data, status=True)
        else:
            return  api_response(404,"No Course found",{},status=False)





class AdminBlockCourseView(APIView):
    """
            Admin can block by any course by using course id.
    """
    permission_classes = (IsAdminUser,)

    def put(self,request):
        try:
            course_id = request.data.get("id", None)
            course = Course.objects.get(id=course_id)
            if course.block_by_admin == False:
                course.block_by_admin = True
                course.save()
                return api_response(200, "Blocked by admin  successfully", request.data, status=True)
            elif course.block_by_admin == True:
                course.block_by_admin = False
                course.save()
                return api_response(200, "Unblocked by admin  successfully", {}, status=True)
        except Course.DoesNotExist:
            return api_response(400, "Course Not Found", {}, status=False)


class AdminCourseBookingDetailView(APIView):
    """
        teacher get the details of course booking.
    """
    permission_classes = (IsAdminUser,)

    def post(self, request):
        course_id = request.data.get("id", None)
        booking_course = CourseBooking.objects.filter(course__id=course_id,is_booking=True).order_by('-purchase_at')
        # print(booking_course)
        if booking_course:
            serializer = AdminCourseBookingSerializer(booking_course, many=True)
            return api_response(200, "Admin Course booking retrieved successfully.", serializer.data, status=True)
        else:
            return api_response(200, "No Course booking found", [], status=True)


class AdminCourseReportGetView(APIView):
    permission_classes = (IsAdminUser,)

    def post(self,request):
        user = request.user.id
        teacher_id = request.data.get("id", None)
        report = CourseReport.objects.filter(teacher_id=teacher_id)
        print(report)
        if report:
            serialized_report = AdminCourseReportGetSerializer(report,many=True)
            return api_response(200,"Course report retrived successfully", serialized_report.data, status=True)
        else:
            return api_response(200, "No Course report found", [], status=True)


