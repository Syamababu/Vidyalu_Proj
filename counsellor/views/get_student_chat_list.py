from rest_framework.views import APIView

from core.helpers import api_response
from core.permissions import IsCounsellor
from core.models.users import User

from student.models.session_booking import SessionBooking
from counsellor.serializers.get_student_chat_list_serializer import StudentChatListSerializer


import sys

class StudentChatList(APIView):
    permission_classes = (IsCounsellor,)
    def get(self,request):
        try:
            counsellor_id = request.user.id
            student_list = SessionBooking.objects.filter(counsellor_id=counsellor_id,is_booking=True).values("user_id").distinct()
            student_details = User.objects.filter(id__in = student_list)
            serializer = StudentChatListSerializer(student_details,many = True,context = {"counsellor":counsellor_id})

            return api_response(200, "Student chat list retrieved successfully.", serializer.data, status=True)
        except:
            print(sys.exc_info())
            return api_response(400, "Student chat list retrive faild", {}, status=True)