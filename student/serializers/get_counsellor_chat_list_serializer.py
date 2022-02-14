from rest_framework import serializers

from core.models.users import User
from core.models.user_status_models import UserStatus

from chat.models import Thread, Message

from counsellor.models.counsellors import Counsellor

from counsellor.serializers.counsellor_serializer import CounsellorSerializer

class CounsellorChatListSerializer(serializers.ModelSerializer):
    active_status = serializers.SerializerMethodField()
    unseen_message_count = serializers.SerializerMethodField()
    counsellor = serializers.SerializerMethodField()

    class Meta:
        model = User
        # fields = ('id','email','username','full_name','profile_image','active_status','unseen_message_count')
        fields =('active_status','unseen_message_count','counsellor')

    def get_active_status(self, obj):
        try:
            # teacher_id = obj.id
            counsellor = UserStatus.objects.get(user_id = obj.id)
            return counsellor.active_status
        except UserStatus.DoesNotExist:
            return None
    
    def get_counsellor(self,obj):
        try:
            counsellor_id = obj.id
            counsellor = Counsellor.objects.get(counsellor_id=counsellor_id)
            serializer1 = CounsellorSerializer(counsellor)
            data1 = serializer1.data
            return data1
        except Counsellor.DoesNotExist:
            return None

    def get_unseen_message_count(self, obj):
        try:
            thread_obj = Thread.objects.get_or_create_personal_thread(obj,self.context.get('student'))
            message_count = Message.objects.filter(thread = thread_obj, sender = obj, is_seen = False).count()
            return message_count
        except:
            return None