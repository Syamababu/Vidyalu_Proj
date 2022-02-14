from rest_framework.views import APIView
from teacher.serializers.course_serializers import CourseDetailSerializer
from counsellor.serializers.session_serializers import SessionDetailSerializer
from teacher.models.courses_model import Course
from core.helpers import api_response
from core.permissions import IsStudent
from student.models.course_booking import CourseBooking
from django.utils import timezone
from counsellor.models.session_model import Session
from student.models.session_booking import SessionBooking
import operator
from student.serializers.student_dashboard_serializer import PopularCourseSerializer,PopularSessionSerializer
from django.db.models import Case,When



class StudentRunningPastCoursesView(APIView):
    """
        teacher get the course details.
    """
    permission_classes = (IsStudent,)

    def get(self, request):
        user = request.user.id
        booked_course = CourseBooking.objects.filter(user_id = user,is_booking = True)
        courses_id = booked_course.values_list("course_id")
        if courses_id:
            current_date = timezone.now().date()
            course = Course.objects.filter(id__in=courses_id)
            past_course = course.filter(end_date__lt=current_date)[:3]
            live_course = course.filter(start_date__lte=current_date, end_date__gte=current_date)[:3]
            serializer1 = CourseDetailSerializer(instance=past_course, many=True)
            serializer2 = CourseDetailSerializer(instance=live_course, many=True)
            return api_response(200, "Course details retrieved successfully.", {"live_course": serializer2.data,"past_course": serializer1.data},status=True)
        else:
            return api_response(200, "No Course found", [], status=True)



class StudentRunningPastSessionsView(APIView):
    """
           counsellor get the session .
    """
    permission_classes = (IsStudent,)

    def get(self, request):
        user = request.user.id
        booked_session = SessionBooking.objects.filter(user_id=user, is_booking=True)
        sessions_id = booked_session.values_list("session_id")
        print(sessions_id)

        if sessions_id:
            current_date = timezone.now().date()
            session = Session.objects.filter(id__in=sessions_id)
            past_session = session.filter(end_date__lt=current_date)[:3]
            live_session = session.filter(start_date__lte=current_date, end_date__gte=current_date)[:3]
            serializer1 = SessionDetailSerializer(instance=past_session, many=True)
            serializer2 = SessionDetailSerializer(instance=live_session, many=True)
            # serializer = SessionDetailSerializer(session, many=True)
            return api_response(200, "Session details retrieved successfully.",
                                {"past_session": serializer1.data,"live_session": serializer2.data,}, status=True)

        else:
            return api_response(200, "No Session found", [], status=True)


class StudentPopularCourseView(APIView):
    permission_classes = (IsStudent,)

    def get(self, request):
        booked_course = CourseBooking.objects.all()
        if booked_course:
            course=[]
            d=[]
            for obj in booked_course:
                if obj.course_id not in course:
                    course.append(obj.course_id)
            for cid in course:
                cont = CourseBooking.objects.filter(course_id=cid).count()
                d.append({"course_id":cid,"count":cont})

            sort_course = sorted(d,key=lambda k:k["count"],reverse=True)[:5]
            courses_id = [item["course_id"] for item in sort_course]
            preserved = Case(*[When(pk=pk, then=pos) for pos, pk in enumerate(courses_id)])
            course = Course.objects.filter(id__in=courses_id).order_by(preserved)
            serializer = PopularCourseSerializer(course,many=True)
            return api_response(200, "Course retrieved successfully.", serializer.data ,status=True)
        else:
            return api_response(200, "No Course found", [], status=True)

  # res = {course[i]: d[i] for i in range(len(course))}
            # print(res)
            # print(res)
            # print({k: v for k, v in sorted(res.items(), key=lambda item: item[1])})
            # sorted_d = dict(sorted(res.items(), key=operator.itemgetter(1), reverse=True))
            # dict(sorted(res.items(), key=operator.itemgetter(1), reverse=True)[:5])
            # newA = dict(sorted(d.items(), key=operator.itemgetter(1), reverse=True)[:5])
            # print(newA)

class StudentPopularSessionView(APIView):
    permission_classes = (IsStudent,)

    def get(self, request):
        booked_session = SessionBooking.objects.all()
        if booked_session:
            session = []
            d = []
            for obj in booked_session:
                if obj.session_id not in session:
                    session.append(obj.session_id)
            for cid in session:
                cont = SessionBooking.objects.filter(session_id=cid).count()
                d.append({"session_id": cid,"count":cont})

            sort_session = sorted(d, key=lambda k: k["count"], reverse=True)[:5]
            session_id = [item["session_id"] for item in sort_session]
            preserved = Case(*[When(pk=pk, then=pos) for pos, pk in enumerate(session_id)])
            session = Session.objects.filter(id__in=session_id).order_by(preserved)
            serializer = PopularSessionSerializer(session, many=True)
            return api_response(200, "Session retrieved successfully.", serializer.data, status=True)
        else:
            return api_response(200, "No Session found", [], status=True)



        #     res = {session[i]: d[i] for i in range(len(session))}
        #     # print(res)
        #     # print({k: v for k, v in sorted(res.items(), key=lambda item: item[1])})
        #     # sorted_d = dict(sorted(res.items(), key=operator.itemgetter(1), reverse=True))
        #     # dict(sorted(res.items(), key=operator.itemgetter(1), reverse=True)[:5])
        #     newA = dict(sorted(res.items(), key=operator.itemgetter(1), reverse=True)[:5])
        #     print(newA)
        #     session_id = []
        #     for key in newA.keys():
        #         session_id.append(key)
        #     print(session_id)
        #
        #     session = Session.objects.filter(id__in=session_id)
        #     serializer = PopularSessionSerializer(session, many=True)
        #     return api_response(200, "Course retrieved successfully.", serializer.data, status=True)
        # else:
        #     return api_response(200, "No Course found", [], status=True)

# class StudentPastCoursesView(APIView):
#     """
#         teacher get the course details.
#     """
#     permission_classes = (IsStudent,)
#
#     def get(self, request):
#         user = request.user.id
#         booked_course = CourseBooking.objects.filter(user_id=user, is_booking=True)
#         courses_id = booked_course.values_list("course_id")
#         print(courses_id)
#         if courses_id:
#             current_date = timezone.now().date()
#             course = Course.objects.filter(id__in=courses_id)
#             past_course = course.filter(end_date__lt=current_date)
#             serializer1 = CourseDetailSerializer(instance=past_course, many=True)
#             return api_response(200, "Course details retrieved successfully.",{"past_course": serializer1.data}, status=True)
#
#         else:
#             return api_response(200, "No Course found", [], status=True)
#























