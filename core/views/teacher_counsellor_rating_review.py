from django.db.models import Avg

from rest_framework.views import APIView

from core.permissions import IsStudent

from student.models.course_rating import CourseRating
from student.models.session_rating import SessionRating
from student.models.course_booking import CourseBooking
from student.models.session_booking import SessionBooking

from teacher.models.courses_model import Course
from counsellor.models.session_model import Session

from core.helpers import api_response
from core.models.users import User
from rest_framework.permissions import IsAuthenticated
from core.permissions import IsTeacherCounsellor
from vidyalu_admin.models.course_session_category_models import CourseSesssionCategoryModel
from vidyalu_admin.serializers.course_session_category_serializer import CourseSessionCategorySerializer


import sys

class TeacherCounsellorRatingReview(APIView):
    # permission_classes = (IsAuthenticated,)

    def post(self, request):
        try:
            user = User.objects.get(id = request.data['id'])
            user_role = user.role
            if user_role == 'teacher':
                user_ratings = CourseRating.objects.filter(teacher = user)
                # print(user_ratings.count())
                average_rating = user_ratings.aggregate(average_rating = Avg('rating'))
                print(average_rating)
                course_count = Course.objects.filter(teacher = user).count()
                student_count = CourseBooking.objects.filter(teacher = user).count()
                # rating_sum = user_ratings.rating.sum()
                return api_response(200, "Review rating count successfully fetched",
                    [{'total_reviews':user_ratings.count(),'total_course':course_count,'total_students':student_count,'average_rating':average_rating['average_rating']}],
                    status=True)
            elif user_role == 'counsellor':
                user_ratings = SessionRating.objects.filter(counsellor = user)
                # print(user_ratings.count())
                average_rating = user_ratings.aggregate(average_rating = Avg('rating'))
                print(average_rating)
                session_count = Session.objects.filter(counsellor = user).count()
                student_count = SessionBooking.objects.filter(counsellor = user).count()
                # rating_sum = user_ratings.rating.sum()
                return api_response(200, "Review rating count successfully fetched",
                    [{'total_reviews':user_ratings.count(),'total_course':session_count,'total_students':student_count,'average_rating': 0 if average_rating['average_rating'] == None else average_rating['average_rating']}],
                    status=True)
            else:
                return api_response(400, "Review rating count retrive failed", {}, status=False)
        except:
            print(sys.exc_info())
            return api_response(400, "Review rating count retrive failed", {}, status=False)



class GetCourseSessionCategoryView(APIView):
    permission_classes = (IsTeacherCounsellor,)

    def post(self, request):
        try:
            category_type = request.data['category_type']
            serializer = CourseSessionCategorySerializer(CourseSesssionCategoryModel.objects.filter(category_type=category_type,is_active=True), many=True)
            return api_response(200, 'category fetched successfully', serializer.data, status=True)
        except:
            serializer = CourseSessionCategorySerializer(CourseSesssionCategoryModel.objects.all(), many=True)
            return api_response(200, 'category fetched successfully', serializer.data, status=True)



