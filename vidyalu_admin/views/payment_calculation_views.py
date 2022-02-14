from rest_framework.views import APIView

from core.permissions import IsAdmin
from core.helpers import api_response

from student.models.course_booking import CourseBooking
from student.models.students import Student
from student.serializers.student_serializer import StudentSerializer

from student.models.session_booking import SessionBooking


class PaymentCalculationCourseView(APIView):

    permission_classes = (IsAdmin,)


    def post(self, request):
        try:
            course_id = request.data['course_id']
            course_booked_students = CourseBooking.objects.filter(course_id = course_id)

            course_revenue = 0
            course_revenue_distribution_studentwise = []

            for i in course_booked_students:
                    student = Student.objects.get(student = i.user.id)
                    serializer = StudentSerializer(instance=student)
                    course_revenue_distribution_studentwise.append({'student_details': serializer.data, 'admin_money':0.15*i.amount_paid, 'teacher_money': i.amount_paid - (0.15*i.amount_paid)})
                    course_revenue += i.amount_paid

            admin_money = 0.15 * course_revenue
            teacher_money = course_revenue - admin_money

            course_revenue_distribution = {'course_revenue': course_revenue, 'admin_money':admin_money, 'teacher_money':teacher_money}

            return api_response(200, "Course revenue distribution fetched", [{'course_revenue_distribution':[course_revenue_distribution], 'revenue_distribution_studentwise':course_revenue_distribution_studentwise}], status= True)

        except:
            return api_response(400, "course revenue distribution fetching failed", {}, status=False)

class PaymentCalculationSessionView(APIView):
    
    permission_classes = (IsAdmin,)

    def post(self, request):
        try:
            session_id = request.data['session_id']
            session_booked_students = SessionBooking.objects.filter(session_id = session_id)

            session_revenue = 0

            session_revenue_distribution_studentwise = []

            for i in session_booked_students:
                student = Student.objects.get(student = i.user.id)
                serializer = StudentSerializer(instance=student)
                session_revenue_distribution_studentwise.append({'student_details':serializer.data, 'admin_money': 0.15*i.amount_paid, 'counsellor_money': i.amount_paid - (0.15*i.amount_paid)})
                session_revenue += i.amount_paid

            admin_money = 0.15 * session_revenue
            counsellor_revenue = session_revenue - admin_money

            session_revenue_distribution = {'session_revenue': session_revenue, 'admin_money':admin_money, 'counsellor_money':counsellor_revenue}

            return api_response(200, "Session revenue distribution fetched", [{'course_revenue_distribution':[session_revenue_distribution], 'revenue_distribution_studentwise':session_revenue_distribution_studentwise}], status= True)

        except:
            return api_response(400, "session revenue distribution fetching failed", {}, status = False)
