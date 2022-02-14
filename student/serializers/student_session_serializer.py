from rest_framework import serializers
from counsellor.models.session_model import Session
from counsellor.serializers.counsellor_serializer import CounsellorSerializer
from counsellor.models.counsellors import Counsellor
from student.models.session_booking import SessionBooking
from student.models.session_rating import SessionRating
from student.serializers.session_rating_serializer import SessionRatingGetSerializer
from django.db.models import Avg
from student.models.student_session_report import SessionReport
from student.serializers.session_report_serializer import SessionReportGetSerializer


class SessionDetailSerializer(serializers.ModelSerializer):
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


class OneSessionDetailSerializer(serializers.ModelSerializer):
    """
           serializer for get  the single session list.
    """
    counsellor_details = serializers.SerializerMethodField()
    is_booking = serializers.SerializerMethodField()
    is_rating = serializers.SerializerMethodField()
    is_report = serializers.SerializerMethodField()

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

    def get_is_booking(self, obj):
        # request = self.context['request']
        try:
            user_id = self.context['user_id']
            session_id = obj.id
            if user_id == obj.counsellor.id:
                return True
            bid = SessionBooking.objects.get(user__id=user_id, session__id=session_id)
            return bid.is_booking
        except:
            return False


    def get_is_rating(self, obj):
        try:
            user_id=self.context['user_id']
            session_id=obj.id
            # if user_id==obj.teacher.id:
            #     return True
            bid = SessionRating.objects.get(user_id=user_id, session_id=session_id)
            if bid:
                serializer1 = SessionRatingGetSerializer(bid)
                data1 = serializer1.data
                return [data1]
            else:
                return []
        except:
            return  []
   

    def get_is_report(self, obj):
        try:
            user_id = self.context['user_id']
            session_id = obj.id
            # if user_id==obj.teacher.id:
            #     return True
            bid = SessionReport.objects.get(user_id=user_id, session_id=session_id)
            if bid:
                serializer1 = SessionReportGetSerializer(bid)
                data1 = serializer1.data
                return [data1]
            else:
                return []
        except:
            return []

class OneSessionDetailOnlySerializer(serializers.ModelSerializer):
    """
           serializer for get  the single session list.
    """
    counsellor_details = serializers.SerializerMethodField()
    # is_booking = serializers.SerializerMethodField()
    is_rating = serializers.SerializerMethodField()
    is_report = serializers.SerializerMethodField()

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

    # def get_is_booking(self, obj):
    #     # request = self.context['request']
    #     try:
    #         user_id = self.context['user_id']
    #         session_id = obj.id
    #         if user_id == obj.counsellor.id:
    #             return True
    #         bid = SessionBooking.objects.get(user__id=user_id, session__id=session_id)
    #         return bid.is_booking
    #     except:
    #         return False


    def get_is_rating(self, obj):
        try:
            user_id=self.context['user_id']
            session_id=obj.id
            # if user_id==obj.teacher.id:
            #     return True
            bid = SessionRating.objects.get(user_id=user_id, session_id=session_id)
            if bid:
                serializer1 = SessionRatingGetSerializer(bid)
                data1 = serializer1.data
                return [data1]
            else:
                return []
        except:
            return  []
   

    def get_is_report(self, obj):
        try:
            user_id = self.context['user_id']
            session_id = obj.id
            # if user_id==obj.teacher.id:
            #     return True
            bid = SessionReport.objects.get(user_id=user_id, session_id=session_id)
            if bid:
                serializer1 = SessionReportGetSerializer(bid)
                data1 = serializer1.data
                return [data1]
            else:
                return []
        except:
            return []










