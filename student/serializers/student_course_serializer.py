from rest_framework import serializers
from teacher.models.courses_model import Course
from teacher.serializers.teacher_serializer import TeacherSerializer
from teacher.models.teachers import Teacher
from core.models.users import User
from student.models.course_booking import CourseBooking
from student.models.course_rating import CourseRating
from student.serializers.course_rating_serializer import CourseRatingGetSerializer
from student.serializers.course_report_serializer import CourseReportGetSerializer
from student.models.student_course_report import CourseReport

from django.db.models import Avg


class CourseDetailSerializer(serializers.ModelSerializer):
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



class OneCourseDetailSerializer(serializers.ModelSerializer):
    """
           serializer for get  the single course list.
    """
    # contents = serializers.FileField(read_only=True)
    # video = serializers.FileField(read_only=True)

    teacher_details = serializers.SerializerMethodField()
    is_booking = serializers.SerializerMethodField()
    is_rating = serializers.SerializerMethodField()
    is_report = serializers.SerializerMethodField()

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

    def get_is_booking(self, obj):
        try:
            user_id=self.context['user_id']
            course_id=obj.id
            if user_id==obj.teacher.id:
                return True
            bid = CourseBooking.objects.get(user__id=user_id, course__id=course_id)
            return bid.is_booking
        except:
            return  False

    def get_is_rating(self, obj):
        try:
            user_id=self.context['user_id']
            course_id=obj.id
            # if user_id==obj.teacher.id:
            #     return True
            bid = CourseRating.objects.get(user_id=user_id, course_id=course_id)
            if bid:
                serializer1 = CourseRatingGetSerializer(bid)
                data1 = serializer1.data
                return [data1]
            else:
                return []
        except:
            return  []
   

    def get_is_report(self, obj):
        try:
            user_id = self.context['user_id']
            course_id = obj.id
            # if user_id==obj.teacher.id:
            #     return True
            bid = CourseReport.objects.get(user_id=user_id, course_id=course_id)
            if bid:
                serializer1 = CourseReportGetSerializer(bid)
                data1 = serializer1.data
                return [data1]
            else:
                return []
        except:
            return []

class OneCourseDetailOnlySerializer(serializers.ModelSerializer):
    """
           serializer for get  the single course list.
    """
    # contents = serializers.FileField(read_only=True)
    # video = serializers.FileField(read_only=True)

    teacher_details = serializers.SerializerMethodField()
    # is_booking = serializers.SerializerMethodField()
    is_rating = serializers.SerializerMethodField()
    is_report = serializers.SerializerMethodField()

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

    # def get_is_booking(self, obj):
    #     try:
    #         user_id=self.context['user_id']
    #         course_id=obj.id
    #         if user_id==obj.teacher.id:
    #             return True
    #         bid = CourseBooking.objects.get(user__id=user_id, course__id=course_id)
    #         return bid.is_booking
    #     except:
    #         return  False

    def get_is_rating(self, obj):
        try:
            user_id=self.context['user_id']
            course_id=obj.id
            # if user_id==obj.teacher.id:
            #     return True
            bid = CourseRating.objects.get(user_id=user_id, course_id=course_id)
            if bid:
                serializer1 = CourseRatingGetSerializer(bid)
                data1 = serializer1.data
                return [data1]
            else:
                return []
        except:
            return  []
   

    def get_is_report(self, obj):
        try:
            user_id = self.context['user_id']
            course_id = obj.id
            # if user_id==obj.teacher.id:
            #     return True
            bid = CourseReport.objects.get(user_id=user_id, course_id=course_id)
            if bid:
                serializer1 = CourseReportGetSerializer(bid)
                data1 = serializer1.data
                return [data1]
            else:
                return []
        except:
            return []







