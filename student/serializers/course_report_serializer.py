from rest_framework import serializers
from student.models.student_course_report import CourseReport
from core.serializers.auth_serializer import UserSerializer
from teacher.serializers.course_serializers import CourseDetailSerializer
from teacher.models.courses_model import Course
from teacher.serializers.teacher_serializer import TeacherSerializer
from teacher.models.teachers import Teacher
from student.serializers.student_serializer import StudentSerializer
from student.models.students import Student
from core.models.users import User

class CourseReportSerializer(serializers.ModelSerializer):
    """
            serializer for student can report the course.
    """
    # name = serializers.SerializerMethodField()
    class Meta:
        model = CourseReport
        exclude = ("user",)

    # def get_name(self, obj):
    #     try:
    #         stu_id = obj.user_id
    #         tch = User.objects.get(id=stu_id)
    #         # serializer1 = TeacherSerializer(tch)
    #         # data1 = serializer1.data
    #         return tch.username
    #     except User.DoesNotExist:
    #         return None


class CourseReportGetSerializer(serializers.ModelSerializer):

    # student_details = serializers.SerializerMethodField()
    # teacher_details = serializers.SerializerMethodField()
    class Meta:
        model = CourseReport
        fields = '__all__'

    # def get_student_details(self, obj):
    #     try:
    #         stu_id = obj.user_id
    #         stu = Student.objects.get(student_id=stu_id)
    #         serializer1 = StudentSerializer(stu)
    #         data1 = serializer1.data
    #         return data1
    #     except User.DoesNotExist:
    #         return None
    #
    # def get_teacher_details(self, obj):
    #     try:
    #         tch_id = obj.teacher_id
    #         tch = Teacher.objects.get(teacher_id=tch_id)
    #         serializer1 = TeacherSerializer(tch)
    #         data1 = serializer1.data
    #         return data1
    #     except User.DoesNotExist:
    #         return None


 # serializer1 = TeacherSerializer(tch)
            # data1 = serializer1.data