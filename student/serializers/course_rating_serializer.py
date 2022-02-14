from rest_framework import serializers
from student.models.course_rating import CourseRating
from core.serializers.auth_serializer import UserSerializer
from teacher.serializers.course_serializers import CourseDetailSerializer
from teacher.models.courses_model import Course
from teacher.serializers.teacher_serializer import TeacherSerializer
from teacher.models.teachers import Teacher
from core.models.users import User

class CourseRatingSerializer(serializers.ModelSerializer):
    """
              serializer for student can rate the course.
    """
    name = serializers.SerializerMethodField()
    class Meta:
        model = CourseRating
        exclude = ("user",)

    def get_name(self, obj):
        try:
            stu_id = obj.user_id
            tch = User.objects.get(id=stu_id)
            # serializer1 = TeacherSerializer(tch)
            # data1 = serializer1.data
            return tch.username
        except User.DoesNotExist:
            return None






class CourseRatingGetSerializer(serializers.ModelSerializer):
    # course = CourseDetailSerializer()
    # teacher = UserSerializer()
    name = serializers.SerializerMethodField()
    class Meta:
        model = CourseRating
        fields = '__all__'

    def get_name(self, obj):
        try:
            stu_id = obj.user_id
            tch = User.objects.get(id=stu_id)
            # serializer1 = TeacherSerializer(tch)
            # data1 = serializer1.data
            return tch.username
        except User.DoesNotExist:
            return None



class CourseReviewGetSerializer(serializers.ModelSerializer):
    name =serializers.SerializerMethodField()

    class Meta:
        model = CourseRating
        fields = '__all__'

    def get_name(self, obj):
        try:
            stu_id = obj.user_id
            tch = User.objects.get(id=stu_id)
            # serializer1 = TeacherSerializer(tch)
            # data1 = serializer1.data
            return tch.username
        except User.DoesNotExist:
            return None




#

# class CourseBookingGetSerializer(serializers.ModelSerializer):
#     course = CourseDetailSerializer()
#     # teacher = UserSerializer()
#     teacher = serializers.SerializerMethodField()
#
#     class Meta:
#         model = CourseBooking
#         fields = '__all__'
#
#     def get_teacher(self, obj):
#         try:
#             tch_id=obj.teacher.id
#             tch = Teacher.objects.get(teacher_id=tch_id)
#             serializer1 = TeacherSerializer(tch)
#             data1 = serializer1.data
#             return data1
#         except Teacher.DoesNotExist:
#             return None

