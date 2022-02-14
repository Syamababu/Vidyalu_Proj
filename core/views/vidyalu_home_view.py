from rest_framework.views import APIView
from teacher.models.courses_model import Course
from core.helpers import api_response
from student.models.course_booking import CourseBooking
from counsellor.models.session_model import Session
from student.models.session_booking import SessionBooking
import operator
from core.serializers.vidyalu_home_serializer import PopularCourseallSerializer,PopularSessionallSerializer,PopularTeacherallSerializer,PopularCounsellorSerializer
from django.db.models import Case,When
from rest_framework.permissions import IsAuthenticated
from teacher.models.teachers import Teacher
from counsellor.models.counsellors import Counsellor
from core.models.users import User



class PopularCourselistView(APIView):
    #permission_classes = (IsAuthenticated,)

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

            sort_course = sorted(d,key=lambda k:k["count"],reverse=True)[:8]
            courses_id = [item["course_id"] for item in sort_course]
            print(courses_id)
            preserved = Case(*[When(pk=pk, then=pos) for pos, pk in enumerate(courses_id)])
            course = Course.objects.filter(id__in=courses_id).order_by(preserved)
            serializer = PopularCourseallSerializer(course,many=True)
            return api_response(200, "Popular Course retrieved successfully.", serializer.data ,status=True)
        else:
            return api_response(200, "No Popular Course found", [], status=True)



class PopularSessionlistView(APIView):
    #permission_classes = (IsAuthenticated,)

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

            sort_session = sorted(d, key=lambda k: k["count"], reverse=True)[:8]
            session_id = [item["session_id"] for item in sort_session]
            preserved = Case(*[When(pk=pk, then=pos) for pos, pk in enumerate(session_id)])
            session = Session.objects.filter(id__in=session_id).order_by(preserved)
            serializer = PopularSessionallSerializer(session, many=True)
            return api_response(200, "Popular Session retrieved successfully.", serializer.data, status=True)
        else:
            return api_response(200, "No Popular Session found", [], status=True)


class PopularTeacherlistView(APIView):
    #permission_classes = (IsAuthenticated,)

    def get(self, request):
        booked_course = CourseBooking.objects.all()
        if booked_course:
            teacher = []
            d = []
            for obj in booked_course:
                if obj.teacher_id not in teacher:
                    teacher.append(obj.teacher_id)
            for tid in teacher:
                cont = CourseBooking.objects.filter(teacher_id=tid).count()
                d.append({"teacher_id": tid, "count": cont})

            sort_teacher = sorted(d, key=lambda k: k["count"], reverse=True)[:8]
            teacher_id = [item["teacher_id"] for item in sort_teacher]
            print('teacher_id',teacher_id)
            preserved = Case(*[When(pk=pk, then=pos) for pos, pk in enumerate(teacher_id)])
            # course = Course.objects.filter(id__in=teacher_id).order_by(preserved)
            teacher = Teacher.objects.filter(teacher_id__in=teacher_id).order_by(preserved)
            serializer = PopularTeacherallSerializer(teacher, many=True)
            return api_response(200, "Popular Teacher retrieved successfully.", serializer.data, status=True)
        else:
            return api_response(200, "No Popular Teacher found", [], status=True)




class PopularCounsellorlistView(APIView):
    #permission_classes = (IsAuthenticated,)

    def get(self, request):
        booked_session = SessionBooking.objects.all()
        if booked_session:
            counsellor = []
            d = []
            for obj in booked_session:
                if obj.counsellor_id not in counsellor:
                    counsellor.append(obj.counsellor_id)
            for cid in counsellor:
                cont = SessionBooking.objects.filter(counsellor_id=cid).count()
                d.append({"counsellor_id": cid,"count":cont})

            sort_counsellor = sorted(d, key=lambda k: k["count"], reverse=True)[:8]
            counsellor_id = [item["counsellor_id"] for item in sort_counsellor]
            preserved = Case(*[When(pk=pk, then=pos) for pos, pk in enumerate(counsellor_id)])
            counsellor = Counsellor.objects.filter(counsellor_id__in=counsellor_id).order_by(preserved)
            serializer = PopularCounsellorSerializer(counsellor, many=True)
            return api_response(200, "Popular Counsellor retrieved successfully.", serializer.data, status=True)
        else:
            return api_response(200, "No Popular Counsellor found", [], status=True)























