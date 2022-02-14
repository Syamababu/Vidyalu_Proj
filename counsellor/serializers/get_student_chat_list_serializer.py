from rest_framework import serializers

from core.models.users import User
from core.models.user_status_models import UserStatus

from student.models.students import Student
from student.serializers.student_serializer import StudentSerializer

from chat.models import Thread, Message

# import sys

class StudentChatListSerializer(serializers.ModelSerializer):

    active_status = serializers.SerializerMethodField()
    unseen_message_count = serializers.SerializerMethodField()
    student = serializers.SerializerMethodField()

    class Meta:
        model = User
        # fields = ('id','email','username','full_name','profile_image','active_status','unseen_message_count')
        fields =('active_status','student','unseen_message_count')
    
    def get_active_status(self,obj):
        try:
            stu_id = obj.id
            stu = UserStatus.objects.get(user_id=stu_id)
            return stu.active_status
        except UserStatus.DoesNotExist:
            return None

    def get_student(self,obj):
        try:
            stu_id = obj.id
            stu = Student.objects.get(student_id=stu_id)
            serializer1 = StudentSerializer(stu)
            data1 = serializer1.data
            print(data1)
            return data1
        except Student.DoesNotExist:
            return None
    
    def get_unseen_message_count(self, obj):
        try:
            print(obj)
            # obj = Thread.objects.filter(users__in = [obj.id,self.context.get("teacher")])
            thread_obj = Thread.objects.get_or_create_personal_thread(obj,self.context.get("counsellor"))
            message_count = Message.objects.filter(thread = thread_obj, sender = obj, is_seen = False).count()
            return message_count
        except:
            # print(sys.exc_info())
            return None
