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


class PopularCourseSerializer(serializers.ModelSerializer):
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
            tch_id=obj.teacher.id
            tch = Teacher.objects.get(teacher_id=tch_id)
            serializer1 = TeacherSerializer(tch)
            data1 = serializer1.data
            return data1
        except Teacher.DoesNotExist:
            return None

    def get_review_count(self, obj):
        review_count = CourseRating.objects.filter(course_id = obj.id).count()
        return review_count
    
    def get_average_rating(Self, obj):
        user_ratings = CourseRating.objects.filter(course_id = obj.id)
        average_rating = user_ratings.aggregate(average_rating = Avg('rating'))
        return 0 if average_rating['average_rating'] == None else average_rating['average_rating']






class PopularSessionSerializer(serializers.ModelSerializer):
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
