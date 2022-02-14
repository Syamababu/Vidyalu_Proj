from rest_framework import serializers

from core.models.users import User
from core.models.user_status_models import UserStatus
from teacher.serializers.teacher_serializer import TeacherSerializer
from chat.models import Thread, Message
from teacher.models.teachers import Teacher

import sys

class TeacherChatListSerializer(serializers.ModelSerializer):
    active_status = serializers.SerializerMethodField()
    unseen_message_count = serializers.SerializerMethodField()
    teacher = serializers.SerializerMethodField()

    class Meta:
        model = User
        #fields = ('id','email','username','full_name','profile_image','active_status','unseen_message_count')
        fields =('active_status','unseen_message_count','teacher')

    def get_active_status(self, obj):
        try:
            # teacher_id = obj.id
            teacher = UserStatus.objects.get(user_id = obj.id)
            return teacher.active_status
        except UserStatus.DoesNotExist:
            return None

    def get_teacher(self,obj):
        try:
            tch_id = obj.id
            tch = Teacher.objects.get(teacher_id=tch_id)
            serializer1 = TeacherSerializer(tch)
            data1 = serializer1.data
            return data1
        except Teacher.DoesNotExist:
            return None
    
    def get_unseen_message_count(self, obj):
        try:
            thread_obj = Thread.objects.get_or_create_personal_thread(obj,self.context.get('student'))
            message_count = Message.objects.filter(thread = thread_obj, sender = obj, is_seen = False).count()
            return message_count
        except:
            print(sys.exc_info())
            return None
