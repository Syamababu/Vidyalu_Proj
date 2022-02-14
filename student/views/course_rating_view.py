from rest_framework.views import APIView
from core.permissions import IsStudent
from core.helpers import api_response
from student.serializers.course_rating_serializer import CourseRatingSerializer,CourseRatingGetSerializer,CourseReviewGetSerializer
from student.models.course_rating import CourseRating
from rest_framework.permissions import IsAuthenticated



class StudentCourseRatingView(APIView):
    """
        student can rate the course.
    """
    permission_classes = (IsStudent,)

    def post(self, request):
            user = request.user.id
            serializer = CourseRatingSerializer(data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save(user_id=user)
                return api_response(200, "Course rating successfully", serializer.data, status=True)
            else:
                return api_response(400, "Course rating failed", {}, status=False)



class StudentCourseRatingEditView(APIView):
    """
           student can rate the course.
    """
    permission_classes = (IsStudent,)

    def put(self, request):
        try:
            user = request.user.id
            course_id = request.data.get("course", None)
            course = CourseRating.objects.get(user_id=user,course_id=course_id)
            serializer = CourseRatingSerializer(course, data=request.data, partial=True)
            if serializer.is_valid(raise_exception=True):
                serializer.save(user_id=user)
                return api_response(200, "Course rating Updated successfully", serializer.data, status=True)
            else:
                return api_response(400, "Invalid data", {}, status=False)
        except CourseRating.DoesNotExist:
            return api_response(400, "Course Not Found", {},status=False)



class StudentCourseRatingGetView(APIView):
    permission_classes = (IsStudent,)

    def post(self,request):
        user = request.user.id
        # teacher_id = Teacher.objects.get(teacher_id = user_id).id
        course_id = request.data.get("id", None)
        rating = CourseRating.objects.filter(course_id=course_id)
        print(rating)
        if rating:
            serialized_rating = CourseRatingGetSerializer(rating,many=True)
            return api_response(200,"Course rating retrived successfully", serialized_rating.data, status=True)
        else:
            return api_response(200, "No Course found", [], status=True)

class StudentCourseReviewGetView(APIView):
    # permission_classes = (IsAuthenticated,)

    def post(self,request):
        # user = request.user.id
        # teacher_id = Teacher.objects.get(teacher_id = user_id).id

        try:
            course_id = request.data.get("id", None)
            rating = CourseRating.objects.filter(course_id=course_id)[:5]
            print("rating",rating)
            course_rating = CourseRating.objects.filter(course_id=course_id)
            crs_list = [rat.course.id for rat in course_rating]
            crs_count = len(crs_list)
            print("crs_count",crs_count)
            sum = 0
            for course in course_rating:
                sum += course.rating
            print(sum)
            try:
                avg=sum/crs_count
                print(avg)
                five = CourseRating.objects.filter(course_id=course_id,rating=5).count()
                print(five)
                four = CourseRating.objects.filter(course_id=course_id,rating=4).count()
                print(four)
                three = CourseRating.objects.filter(course_id=course_id,rating=3).count()
                print(three)
                two = CourseRating.objects.filter(course_id=course_id,rating=2).count()
                print(two)
                one = CourseRating.objects.filter(course_id=course_id,rating=1).count()
                print(one)
                d={"total_reviews": crs_count, "avg_rating": avg,"five_rating":five,"four_rating":four,"three_rating":three,"two_rating":two,"one_rating":one}
                res=[]
                res.append(d)
                if rating:
                    serialized_rating = CourseReviewGetSerializer(rating,many=True)
                    # data = serialized_rating.data
                    # print(type(data))
                    # data= data[0]
                    # print(data)
                    data={"rate_review":serialized_rating.data,"rating_count":res}
                    return api_response(200,"Course rating retrived successfully", [data], status=True)
                else:
                    return api_response(200, "No Course found", [], status=True)
            except:
                d = {"total_reviews": 0, "avg_rating": 0, "five_rating": 0, "four_rating": 0,
                     "three_rating": 0, "two_rating": 0, "one_rating": 0}
                res = []
                res.append(d)
                data = {"rate_review": [], "rating_count": res}
                return api_response(200, "No rating found", [data], status=True)
        except CourseRating.DoesNotExist:
            return api_response(400, "Course Not Found", {}, status=False)


# class StudentCourseBookingDetailView(APIView):
#     """
#         student get the details of course booking.
#     """
#     permission_classes = (IsStudent,)
#
#     def get(self, request):
#         booking_course = CourseBooking.objects.filter(user_id=request.user.id,is_booking=True).order_by('-purchase_at')
#         # print(booking_course)
#         if booking_course:
#             serializer = CourseBookingGetSerializer(booking_course, many=True)
#             # serializer.data["teacher"] = [serializer.data["teacher"]]
#             return api_response(200, "Course booking retrieved successfully.", serializer.data, status=True)
#         else:
#             return api_response(200, "No Course booking found", [], status=True)
