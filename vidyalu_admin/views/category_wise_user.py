from rest_framework.views import APIView

from core.permissions import IsAdmin
from core.helpers import api_response
from core.models.users import User

from student.models.course_booking import CourseBooking
from student.models.session_booking import SessionBooking

from core.models.users import User

import sys


class CategoryWiseUser(APIView):
    permission_classes = (IsAdmin,)
    def get(self, request):
        
        try:
            # users = User.objects.filter(role__in = ['student','teacher','counsellor']).distinct()
            # serializer = CategoryWiseUserSerializer()
            # print(serializer.data)
            category_wise_user_count = {'student_count':User.objects.filter(role = 'student').count(),'teacher_count':User.objects.filter(role = 'teacher').count(),
            'counsellor_count':User.objects.filter(role = 'counsellor').count()}

            course_revenue, session_revenue = 0,0
            
            for i in CourseBooking.objects.all():
                course_revenue += i.amount_paid
            
            for i in SessionBooking.objects.all():
                # print(i.session.price)
                session_revenue += i.amount_paid
            
            category_wise_revenue = {'course_revenue':course_revenue,'session_revenue':session_revenue,'total_revenue':course_revenue+session_revenue}
            
            # print(category_wise_user_count)

            students = User.objects.filter(role = 'student')

            failed_student_count = students.filter(is_verified_email = False).count()
            # print(failed_student_count)
            
            students_id = [i.id for i in User.objects.filter(role = 'student', is_verified_email = True)]
            # print(students_id)
            
            course_booked_students_id = [i.user.id for i in CourseBooking.objects.all()]
            # print(course_booked_students_id)

            session_booked_students_id = [i.user.id for i in SessionBooking.objects.all()]
            # print(session_booked_students_id)

            booked_students_id = list(set(course_booked_students_id+session_booked_students_id))
            # print(booked_students_id)

            new_students_count, passed_students_count = 0,0

            for i in students_id:
                if i in booked_students_id:
                    passed_students_count += 1
                else:
                    new_students_count += 1

            category_wise_student = {'failed_student_count':failed_student_count,'new_student_count':new_students_count,'passed_students_count':passed_students_count}



            
            
            
            return api_response(200, "category wise user data fetched",
            [{'category_wise_user_count':category_wise_user_count,'category_wise_revenue':category_wise_revenue,'category_wise_student':category_wise_student}],
            status=True)
        
        except:

            print(sys.exc_info())
            return api_response(400, "category wise user data fetching failed", {}, status=False)
