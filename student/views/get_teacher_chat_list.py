from rest_framework.views import APIView

from core.helpers import api_response
from core.permissions import IsStudent
from core.models.users import User

from student.models.course_booking import CourseBooking
from student.serializers.teacher_chat_list_serializer import TeacherChatListSerializer

import sys

class TeacherChatList(APIView):
    
    permission_classes = (IsStudent,)

    def get(self,request):
        try:
            student_id = request.user.id
            print("student_id", student_id)
            teacher_list = CourseBooking.objects.filter(user_id = student_id, is_booking = True).values('teacher_id').distinct()
            print("teacher_list", teacher_list)
            teacher_details = User.objects.filter(id__in=teacher_list)
            print("teacher_details")
            serializer = TeacherChatListSerializer(teacher_details,many = True,context = {"student":student_id})
            return api_response(200,"Teacher chat list retrived successfully",serializer.data,status=True)
        
        except:
            print(sys.exc_info())
            return api_response(400, "Teacher chat list retrive failed", {}, status = False)