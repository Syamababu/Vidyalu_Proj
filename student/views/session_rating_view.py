from rest_framework.views import APIView
from core.permissions import IsStudent
from core.helpers import api_response
from student.serializers.session_rating_serializer import SessionRatingSerializer,SessionRatingGetSerializer,SessionReviewGetSerializer
from student.models.session_rating import SessionRating
from rest_framework.permissions import IsAuthenticated


class StudentSessionRatingView(APIView):
    """
        student can rate the session .
    """
    permission_classes = (IsStudent,)


    def post(self, request):
            user = request.user.id
            serializer = SessionRatingSerializer(data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save(user_id=user)
                return api_response(200, "Session rating successfully", serializer.data, status=True)
            else:
                return api_response(400, "Session rating failed", {}, status=False)


class StudentSessionRatingEditView(APIView):
    """
            student can rate the session .
    """
    permission_classes = (IsStudent,)

    def put(self, request):
        try:
            user = request.user.id
            session_id = request.data.get("session", None)
            session = SessionRating.objects.get(user_id=user,session_id=session_id)
            serializer = SessionRatingSerializer(session, data=request.data, partial=True)
            if serializer.is_valid(raise_exception=True):
                serializer.save(user_id=user)
                return api_response(200, "Session rating Updated successfully", serializer.data, status=True)
            else:
                return api_response(400, "Invalid data", {}, status=False)
        except SessionRating.DoesNotExist:
            return api_response(400, "Session Not Found", {},status=False)



class StudentSessionRatingGetView(APIView):
    permission_classes = (IsStudent,)

    def post(self,request):
        user = request.user.id
        # teacher_id = Teacher.objects.get(teacher_id = user_id).id
        session_id = request.data.get("id", None)
        rating = SessionRating.objects.filter(session_id=session_id)
        if rating:
            serialized_rating = SessionRatingGetSerializer(rating,many=True)
            return api_response(200,"Session rating retrived successfully", serialized_rating.data, status=True)
        else:
            return api_response(200, "No Session found", [], status=True)

class StudentSessionReviewGetView(APIView):
    # permission_classes = (IsAuthenticated,)

    def post(self,request):
        # user = request.user.id
        # teacher_id = Teacher.objects.get(teacher_id = user_id).id
        try:
            session_id = request.data.get("id", None)
            rating = SessionRating.objects.filter(session_id=session_id)[:5]
            session_rating = SessionRating.objects.filter(session_id=session_id)
            sns_list = [rat.session.id for rat in session_rating]
            sns_count = len(sns_list)
            print(sns_count)
            sum = 0
            for session in session_rating:
                sum += session.rating
            print(sum)
            try:
                avg=sum/sns_count
                print(avg)
                five = SessionRating.objects.filter(session_id=session_id,rating=5).count()
                print(five)
                four = SessionRating.objects.filter(session_id=session_id,rating=4).count()
                print(four)
                three = SessionRating.objects.filter(session_id=session_id,rating=3).count()
                print(three)
                two = SessionRating.objects.filter(session_id=session_id,rating=2).count()
                print(two)
                one = SessionRating.objects.filter(session_id=session_id,rating=1).count()
                print(one)
                d={"total_reviews": sns_count, "avg_rating": avg,"five_rating":five,"four_rating":four,"three_rating":three,"two_rating":two,"one_rating":one}
                res=[]
                res.append(d)
                if rating:
                    serialized_rating = SessionReviewGetSerializer(rating,many=True)
                    # data = serialized_rating.data
                    # print(type(data))
                    # data= data[0]
                    # print(data)
                    data={"rate_review":serialized_rating.data,"rating_count":res}
                    return api_response(200,"Session rating retrived successfully", [data], status=True)
                else:
                    return api_response(200, "No Session found", [], status=True)
            except:
                d = {"total_reviews": 0, "avg_rating": 0, "five_rating": 0, "four_rating": 0,
                     "three_rating": 0, "two_rating": 0, "one_rating": 0}
                res = []
                res.append(d)
                data = {"rate_review": [], "rating_count": res}
                return api_response(200, "No rating found", [data], status=True)
        except SessionRating.DoesNotExist:
            return api_response(400, "Session Not Found", {}, status=False)

#
# class StudentSessionBookingDetailView(APIView):
#     """
#        student get the details of session booking.
#     """
#     permission_classes = (IsStudent,)
#
#     def get(self, request):
#         booking_session = SessionBooking.objects.filter(user_id=request.user.id,is_booking=True).order_by('-purchase_at')
#         if booking_session:
#             serializer = SessionBookingGetSerializer(booking_session, many=True)
#             return api_response(200, "Session booking retrieved successfully.", serializer.data, status=True)
#         else:
#             return api_response(200, "No Session booking found", [], status=True)
#

