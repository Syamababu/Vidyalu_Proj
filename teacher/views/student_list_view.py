

from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from core.helpers import api_response
from student.models.course_booking import CourseBooking
from teacher.serializers.student_list_serializer import StudentbookinglistSerializer
from core.models.user_status_models import UserStatus
from core.permissions import IsTeacher
from teacher.models.courses_model import Course



class StudentlistView(APIView):
    """
        teacher get the details of course booking student.
    """

    def post(self, request):
        teacher_id = request.data.get("id", None)
        student_list = CourseBooking.objects.filter(teacher_id=teacher_id,is_booking=True)
        # print(booking_course)
        if student_list:
            serializer = StudentbookinglistSerializer(student_list, many=True)
            return api_response(200, " teacher can view student details  successfully.", serializer.data, status=True)
        else:
            return api_response(200, "No student details found", [], status=True)


class TeacherCountStudentView(APIView):
    permission_classes = (IsTeacher,)

    def get(self,request):
        teacher_id=request.user.id
        if teacher_id:
            student_list = CourseBooking.objects.filter(teacher_id=teacher_id,is_booking=True)
            stu_list = [stu.user.id for stu in student_list]
            stu_count = len(stu_list)
            # courses_id = student_list.values_list("course_id")
            # course = Course.objects.filter(id__in=courses_id)
            sum = 0
            for course in student_list:
                print(course.course_id)
                course = Course.objects.filter(id=course.course_id)
                for obj in course:
                    sum+=obj.price
            print(sum)
            return api_response(200, "Student count retrieved successfully", [{"stu_count":stu_count,"my_earning":sum}], status=True)
        else:
            return api_response(200, "No student found", [], status=True)