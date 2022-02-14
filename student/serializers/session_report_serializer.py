from rest_framework import serializers
from student.models.student_session_report import SessionReport
from core.models.users import User

from counsellor.serializers.session_serializers import SessionDetailSerializer
from core.serializers.auth_serializer import UserSerializer


class SessionReportSerializer(serializers.ModelSerializer):
    # name = serializers.SerializerMethodField()
    """
              serializer for student can report the session.
    """
    class Meta:
        model = SessionReport
        exclude = ("user",)
    #
    # def get_name(self, obj):
    #     try:
    #         stu_id = obj.user_id
    #         tch = User.objects.get(id=stu_id)
    #         # serializer1 = TeacherSerializer(tch)
    #         # data1 = serializer1.data
    #         return tch.username
    #     except User.DoesNotExist:
    #         return None


class SessionReportGetSerializer(serializers.ModelSerializer):
    # name = serializers.SerializerMethodField()

    class Meta:
        model = SessionReport
        fields = '__all__'

    # def get_name(self, obj):
    #     try:
    #         stu_id = obj.user_id
    #         tch = User.objects.get(id=stu_id)
    #         # serializer1 = TeacherSerializer(tch)
    #         # data1 = serializer1.data
    #         return tch.username
    #     except User.DoesNotExist:
    #         return None


