from time import time
import jwt,requests,json

from django.conf import settings

from rest_framework.views import APIView

from core.helpers import api_response

from core.permissions import IsTeacher,IsCounsellor
from rest_framework.permissions import IsAuthenticated
from video_conferrence.views.zoom_meeting import ZoomMeetings
from video_conferrence.models.zoom_meeting_model import ZoomMeetingCreate
from video_conferrence.serializers.metting_serializers import ZoommettingSerializer
class CreateMeetingURL(APIView):


    def generate_token(self):
        token = jwt.encode(
            
            # Create a payload of the token containing 
            # API Key & expiration time
            {'iss': settings.ZOOM_API_KEY, 'exp': time() + 5000},
            
            # Secret used to generate token signature
            settings.ZOOM_API_SECRET_KEY,
            
            # Specify the hashing alg
            algorithm='HS256'
        )

        print("------------------------------------")
        print(token)
        print("===============================")
        return token


    def meeting_details(self,topic,time,password):
        meetingdetails = {"topic": topic,
                  "type": 2,
                  "start_time": time,
                  "duration": "45",
                  "timezone": "Asia/Kolkata",
                  "password": password,
                  "agenda": "test",
  
                  "recurrence": {"type": 1,
                                 "repeat_interval": 1
                                 },
                  "settings": {"host_video": "true",
                               "participant_video": "true",
                               "join_before_host": "False",
                               "mute_upon_entry": "true",
                               "watermark": "true",
                               "audio": "voip",
                               "auto_recording": "cloud"
                               }
                  }
        return meetingdetails
    
    def create_meeting(self,token,meeting_details):
        headers = {'authorization': 'Bearer %s' % token,
                'content-type': 'application/json'}
        r = requests.post(
            f'https://api.zoom.us/v2/users/suman.mohanty@vaptech.in/meetings',
        headers=headers, json=meeting_details)
        print(meeting_details)
    
        print("\n creating zoom meeting ... \n")
        # print(r.text)
        # converting the output into json and extracting the details
        y = json.loads(r.text)
        print(y)
        join_URL = y["join_url"]
        meeting_password = y["password"]
        meeting_topic = y['topic']
        meeting_time = y['start_time']
    
        # print(
        #     f'\n here is your zoom meeting link {join_URL} and your \
        #     password: "{meetingassword}"\n')
        return {'meeting_url':join_URL,'meeting_password':meeting_password,'meeting_topic':meeting_topic,'meeting_time':meeting_time}

    # permission_classes = (IsAuthenticated,)
    def post(self,request):
        data = request.data

        token = self.generate_token()
        time = data['time']
        topic = data['topic']
        password = data['password']
        meeting_info = self.meeting_details(topic,time,password)
        print(meeting_info)
        # meeting_url,meeting_password = self.create_meeting(token,meeting_info)
        meeting_details_json = self.create_meeting(token,meeting_info)

        return api_response(200,"Meeting url created", meeting_details_json, status=True)




class CreateZoomMeetingURL(APIView):
    # permission_classes = (IsAuthenticated,)
    def post(self, request):
        date =request.data["date"]
        str_topic =request.data["str_topic"]
        str_meeting_duration =request.data["str_meeting_duration"]
        str_meeting_password =request.data["str_meeting_password"]
        zoom_email = 'sumanmohanty123123@gmail.com'
        print(zoom_email)
        api_key = 'fr3wCnoHTymhGUuTu2CNHg'
        secret_key = 'XPWWAM4miC2IZRl4IsqHRWoibaYjaS1w9g1m'
        my_zoom = ZoomMeetings(api_key, secret_key, zoom_email)
        print(my_zoom)
        create_meeting = my_zoom.CreateMeeting(date, str_topic, str_meeting_duration, str_meeting_password)
        print(create_meeting)
        return api_response(201,"metting created",create_meeting,status=True)