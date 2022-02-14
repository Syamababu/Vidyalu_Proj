from rest_framework.views import APIView

from core.helpers import api_response
from core.permissions import IsStudent
from core.models.users import User

from student.models.session_booking import SessionBooking
from student.serializers.get_counsellor_chat_list_serializer import CounsellorChatListSerializer

class CounsellorChatList(APIView):
    
    permission_class = (IsStudent,)

    def get(self,request):
        try:
            student_id = request.user.id
            counsellor_list = SessionBooking.objects.filter(user_id = student_id, is_booking = True).values('counsellor_id').distinct()
            counsellor_details = User.objects.filter(id__in=counsellor_list)
            serializer = CounsellorChatListSerializer(counsellor_details,many = True,context = {"student":student_id})
            return api_response(200,"counsellor chat list retrived successfully",serializer.data,status=True)
        
        except:
            return api_response(400, "counsellor chat list retrive failed", {}, status = False)