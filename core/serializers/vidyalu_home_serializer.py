from rest_framework import serializers
from teacher.models.courses_model import Course
from teacher.serializers.teacher_serializer import TeacherSerializer
from teacher.models.teachers import Teacher
from core.models.users import User
from student.models.course_booking import CourseBooking
from rest_framework import serializers
from counsellor.models.session_model import Session
from counsellor.serializers.counsellor_serializer import CounsellorSerializer
from counsellor.models.counsellors import Counsellor
from student.models.session_booking import SessionBooking
from student.models.session_rating import SessionRating
from student.models.course_rating import CourseRating

from django.db.models import Avg


class PopularCourseallSerializer(serializers.ModelSerializer):
    """
        serializer for get all the course list.
    """
    teacher_details = serializers.SerializerMethodField()
    review_count = serializers.SerializerMethodField()
    average_rating = serializers.SerializerMethodField()

    class Meta:
        model = Course
        exclude = ['date_time']
        extra_fields = ["teacher_details"]

    def get_teacher_details(self, obj):
        try:
            tch_id = obj.teacher.id
            tch = Teacher.objects.get(teacher_id=tch_id)
            serializer1 = TeacherSerializer(tch)
            data1 = serializer1.data
            return data1
        except Teacher.DoesNotExist:
            return None

    def get_review_count(self, obj):
        review_count = CourseRating.objects.filter(course_id=obj.id).count()
        return review_count

    def get_average_rating(Self, obj):
        user_ratings = CourseRating.objects.filter(course_id=obj.id)
        average_rating = user_ratings.aggregate(average_rating=Avg('rating'))
        return 0 if average_rating['average_rating'] == None else average_rating['average_rating']


class PopularSessionallSerializer(serializers.ModelSerializer):
    """
           serializer for get all the session list.
    """
    counsellor_details = serializers.SerializerMethodField()
    # rating_details = serializers.SerializerMethodField()
    review_count = serializers.SerializerMethodField()
    average_rating = serializers.SerializerMethodField()

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

    def get_review_count(self, obj):
        review_count = SessionRating.objects.filter(session_id=obj.id).count()
        return review_count

    def get_average_rating(Self, obj):
        user_ratings = SessionRating.objects.filter(session_id=obj.id)
        average_rating = user_ratings.aggregate(average_rating=Avg('rating'))
        return 0 if average_rating['average_rating'] == None else average_rating['average_rating']


class PopularTeacherallSerializer(serializers.ModelSerializer):
    """
        serializer for get the teacher details.
    """
    review_count = serializers.SerializerMethodField()
    average_rating = serializers.SerializerMethodField()
    email = serializers.CharField(source="teacher.email", read_only=True)
    username = serializers.CharField(source="teacher.username", read_only=True)
    full_name = serializers.CharField(source="teacher.full_name", read_only=True)
    address = serializers.CharField(source="teacher.address", read_only=True)
    state = serializers.CharField(source="teacher.state", read_only=True)
    city = serializers.CharField(source="teacher.city", read_only=True)
    phone = serializers.CharField(source="teacher.phone", read_only=True)
    zip_code = serializers.CharField(source="teacher.area_code", read_only=True)
    profile_img = serializers.ImageField(source="teacher.profile_image", read_only=True)
    photo_url = serializers.CharField(source="teacher.photo_url", read_only=True)
    # profile_img = serializers.SerializerMethodField()


    class Meta:
        model = Teacher
        exclude = ("id",)
        extra_fields = [
            "email",
            "username",
            "full_name",
            "address",
            "state",
            "city",
            "phone",
            "zip_code",
            "profile_img",
            "photo_url",
        ]

    def get_review_count(self, obj):
        review_count = CourseRating.objects.filter(teacher_id=obj.teacher_id).count()
        return review_count

    def get_average_rating(Self, obj):
        user_ratings = CourseRating.objects.filter(teacher_id=obj.teacher_id)
        average_rating = user_ratings.aggregate(average_rating=Avg('rating'))
        return 0 if average_rating['average_rating'] == None else average_rating['average_rating']


class PopularCounsellorSerializer(serializers.ModelSerializer):
    """
            serializer for get the details of counsellor user.
    """
    review_count = serializers.SerializerMethodField()
    average_rating = serializers.SerializerMethodField()
    email = serializers.CharField(source="counsellor.email", read_only=True)
    username = serializers.CharField(source="counsellor.username", read_only=True)
    full_name = serializers.CharField(source="counsellor.full_name", read_only=True)
    address = serializers.CharField(source="counsellor.address", read_only=True)
    state = serializers.CharField(source="counsellor.state", read_only=True)
    city = serializers.CharField(source="counsellor.city", read_only=True)
    phone = serializers.CharField(source="counsellor.phone", read_only=True)
    zip_code = serializers.CharField(source="counsellor.area_code", read_only=True)
    profile_img = serializers.ImageField(source="counsellor.profile_image", read_only=True)
    photo_url = serializers.CharField(source="counsellor.photo_url", read_only=True)
    # provider = serializers.SerializerMethodField()

    class Meta:
        model = Counsellor
        exclude = ("id",)
        extra_fields = [
            "email",
            "username",
            "full_name",
            "address",
            "state",
            "city",
            "phone",
            "zip_code",
            "profile_img",
            "photo_url"
        ]

    def get_review_count(self, obj):
        review_count = SessionRating.objects.filter(counsellor_id=obj.counsellor_id).count()
        return review_count

    def get_average_rating(Self, obj):
        user_ratings = SessionRating.objects.filter(counsellor_id=obj.counsellor_id)
        average_rating = user_ratings.aggregate(average_rating=Avg('rating'))
        return 0 if average_rating['average_rating'] == None else average_rating['average_rating']

    # def get_review_count(self, obj):
    #     review_count = CourseRating.objects.filter(teacher_id=obj.teacher_id).count()
    #     return review_count
    #
    # def get_average_rating(Self, obj):
    #     user_ratings = CourseRating.objects.filter(teacher_id=obj.teacher_id)
    #     average_rating = user_ratings.aggregate(average_rating=Avg('rating'))
    #     return 0 if average_rating['average_rating'] == None else average_rating['average_rating']
