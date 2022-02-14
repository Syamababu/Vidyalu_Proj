from rest_framework.views import APIView

from core.helpers import api_response
from core.permissions import IsTeacher
from core.models.users import User

from student.models.course_booking import CourseBooking
from teacher.serializers.student_chat_list_serializer import StudentChatListSerializer
class StudentChatList(APIView):
    permission_classes = (IsTeacher,)
    def get(self,request):
        try:
            teacher_id = request.user.id
            student_list = CourseBooking.objects.filter(teacher_id=teacher_id,is_booking=True).values("user_id").distinct()
            student_details = User.objects.filter(id__in = student_list)
            serializer = StudentChatListSerializer(student_details,many = True,context = {"teacher":teacher_id})

            return api_response(200, "Student chat list retrieved successfully.", serializer.data, status=True)
        except:
            return api_response(400, "Student chat list retrive faild", serializer.data, status=True)
