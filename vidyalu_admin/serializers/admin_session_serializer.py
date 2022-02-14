from rest_framework import serializers
from counsellor.models.session_model import Session
from counsellor.serializers.counsellor_serializer import CounsellorSerializer
from counsellor.models.counsellors import Counsellor
from student.models.students import Student
from student.serializers.student_serializer import StudentSerializer
from student.models.session_booking import SessionBooking
from student.models.student_session_report import SessionReport


class SessionDetailSerializer(serializers.ModelSerializer):
    """
          serializer for all session details for admin .
      """
    counsellor_details = serializers.SerializerMethodField()

    class Meta:
        model = Session
        exclude = ['date_time']
        extra_fields = ["counsellor_details"]


    def get_counsellor_details(self, obj):
            try:
                cons_id = obj.counsellor.id
                cons = Counsellor.objects.get(counsellor_id=cons_id)
                serializer1 = CounsellorSerializer(cons)
                data1 = serializer1.data
                return data1
            except Counsellor.DoesNotExist:
                return None


class AdminSessionBookingSerializer(serializers.ModelSerializer):
    # course = SessionDetailSerializer()
    # student = StudentSerializer()
    student = serializers.SerializerMethodField()
    class Meta:
        model = SessionBooking
        fields = '__all__'

    def get_student(self, obj):
        try:
            stu_id = obj.user.id
            stu = Student.objects.get(student_id=stu_id)
            serializer1 = StudentSerializer(stu)
            data1 = serializer1.data
            return data1
        except Student.DoesNotExist:
            return None


class AdminSessionDetailSerializer(serializers.ModelSerializer):
    """
              serializer for get  the details of session.
    """
    # name = serializers.CharField(source="counsellor.username", read_only=True)
    class Meta:
        model = Session
        fields = "__all__"
        # exclude = ["teacher"]

class AdminSessionReportGetSerializer(serializers.ModelSerializer):
    # name = serializers.SerializerMethodField()
    student_details = serializers.SerializerMethodField()
    counsellor_details = serializers.SerializerMethodField()
    session_details = serializers.SerializerMethodField()

    class Meta:
        model = SessionReport
        fields = '__all__'

    def get_student_details(self, obj):
        try:
            stu_id = obj.user_id
            stu = Student.objects.get(student_id=stu_id)
            serializer1 = StudentSerializer(stu)
            data1 = serializer1.data
            return data1
        except Student.DoesNotExist:
            return None

    def get_counsellor_details(self, obj):
        try:
            cons_id = obj.counsellor.id
            cons = Counsellor.objects.get(counsellor_id=cons_id)
            serializer1 = CounsellorSerializer(cons)
            data1 = serializer1.data
            return data1
        except Counsellor.DoesNotExist:
            return None

    def get_session_details(self, obj):
        try:
            sns_id = obj.session_id
            sns = Session.objects.get(id=sns_id)
            serializer1 = AdminSessionDetailSerializer(sns)
            data1 = serializer1.data
            return data1
        except Session.DoesNotExist:
            return None




