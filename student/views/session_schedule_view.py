
import pytz
from rest_framework.views import APIView
from django.utils import timezone
from core.permissions import IsStudent
from core.helpers import api_response
import json

from teacher.serializers.course_schedule_serializer import CourseScheduleSerializer
from teacher.models.courses_model import Course,Teacher
from counsellor.models.session_model import Session
from student.models.session_booking import SessionBooking
import datetime as dt
from datetime import datetime
# from pytz import timezone
from dateutil.parser import parse
from core.models.users import User
from datetime import date,timedelta
from django.conf import settings
from django.utils import timezone


"""class CourseScheduleView(APIView):

    permission_classes = (IsTeacher,)
    current_date = timezone.now().date()

    def change_date_time_format(self,date_time_list):
        #Chane
        #[{"class_date": "2021-09-05T18:30:00.000Z", "class_time": "2021-09-02T09:57:38.607Z"}, {"class_date": "2021-09-07T18:30:00.000Z", "class_time": "2021-09-02T09:57:44.086Z"}]
        modified_date_time_list = []
        date_time_list = json.loads(date_time_list)
        for i in date_time_list:
            modified_date_time_list.append({'date_time':i["class_date"].split('T')[0]+'T'+i["class_time"].split('T')[1]})
        print(modified_date_time_list)
        return modified_date_time_list

    def get(self,request):
        user = request.user.id
        teacher = Teacher.objects.get(teacher_id = user)
        classes = CourseSchedule.objects.filter(teacher = teacher,date_time__gte = self.current_date)

        serializer = CourseScheduleSerializer(classes,many = True)

        return api_response(200, "course details saved sucessfully", serializer.data, status=True)

    def post(self, request):
        user = request.user.id
        teacher = Teacher.objects.get(teacher_id = user)
        date_time_list = request.data['date_time_list']
        date_time_list = str(self.change_date_time_format(date_time_list))
        request.data._mutable = True
        request.data['teacher'] = teacher
        request.data['date_time'] = date_time_list
        request.data.pop('date_time_list')
        request.data._mutable = False
        print(request.data)
        serializer = CourseScheduleSerializer(data = request.data,many = True)
        # if serializer.is_valid(raise_exception=True):
        #     try:
        #         serializer.save()
        #     except:
        #         print("lol")

        serializer.is_valid(raise_exception=True)
        serializer.save()

        return api_response(200, "course details saved sucessfully", serializer.data, status=True)"""

class StudentSessionScheduleView(APIView):
    permission_classes = (IsStudent,)

    def change_date_time_format(self,session_date,session_time):
        modified_date_time = session_time.split('T')[0]+'T'+session_date.split('T')[1]
        return modified_date_time

    def get(self,request):
        todaydt = datetime.now()
        todaydt = todaydt + dt.timedelta(hours=5, minutes=30)
        print("current date and time",todaydt)
        user_id = request.user.id
        # teacher_id = Teacher.objects.get(teacher_id = user_id).id
        booking_session = SessionBooking.objects.filter(user_id=request.user.id, is_booking=True)
        session_list =[]
        for obj in booking_session:
            obj.session_id

            # print(booking_course)
            sessions =  Session.objects.filter(publish=True,block_by_admin=False,id=obj.session_id).values("id","title","dates_times","counsellor_id")
            # print(courses)
            # print("----------------------------------")
            # print(courses[0])
            try:
                session_list.append(sessions[0])
            except IndexError:
                pass
        data = []
        time_zone = pytz.timezone('Asia/Kolkata')
        for item in session_list:
            for obj in item['dates_times']:
                obj.update({"counsellor_id":item['counsellor_id'],"id":item["id"],"title":item['title'],"class_date_time":self.change_date_time_format(obj['session_date'],obj['session_time'])})
                data.append(obj)
                date_time_test = parse(obj['class_date_time'])
                print(type(date_time_test))
                # date_time = time_zone.localize(date_time_test)
                utc_date_time = date_time_test.astimezone(pytz.utc)
                utc_time = utc_date_time.time()

                print(date_time_test)
                print(utc_date_time)
                print(utc_time)

                after_2hr_dt = date_time_test + timedelta(minutes=120)
                befor_10min_dt = date_time_test - timedelta(minutes=10)
                print("-------------------------")
                print(befor_10min_dt.date(),"---",befor_10min_dt.time())
                print("ctime",todaydt.date(),"--",todaydt.time())
                print(after_2hr_dt.date(),"---",after_2hr_dt.time())
                if  (todaydt.date() == befor_10min_dt.date()) and (todaydt.time()<after_2hr_dt.time()) and (todaydt.time()>befor_10min_dt.time()):
                    status = True
                else:
                    status = False
                obj.update({"status":status})

                # print(type(date_time_test))
                # print(localize_date_time_no_timezone)
                # print(date_time_test-localize_date_time_no_timezone)

        data.sort(key=lambda x: x['session_date'])
        return api_response(200,"Session reterived successfully", data, status = True)