from datetime import datetime
from django.core.exceptions import ObjectDoesNotExist
import pyotp
from rest_framework.response import Response
from rest_framework.views import APIView
from core.models.users import User
import base64

from core.helpers import api_response

from django.conf import settings

import sys

import requests


class GenerateOTPView(APIView):

    def post(self, request):
        try:
            mobile = User.objects.get(id = request.data['id'])
            mobile.counter += 1
            mobile.save()

            # print(mobile.phone)

            keygen = str(mobile.phone) + str(datetime.date(datetime.now())) + settings.SECRET_KEY
            # print(keygen.returnValue(mobile.phone))

            key = base64.b32encode(keygen.encode())
            OTP = pyotp.HOTP(key)

            # print(OTP.at(mobile.counter))
            # url = "https://www.fast2sms.com/dev/bulkV2"
            # headers = {'authorization': "YOUR API KEY",'Content-Type': "application/x-www-form-urlencoded",'Cache-Control': "no-cache",}
            # payload = "variables_values=5599&route=otp&numbers="+mobile.phone

            # response = requests.request("POST", url, data=payload, headers=headers)

            URL = 'http://www.alots.in/sms-panel/api/http/index.php?username=vtdesign&apikey=5827F-036C0&apirequest=Text&sender=VAPTEC&mobile='+mobile.phone+'&message=Your OTP is : '+OTP.at(mobile.counter)+' VAPTEC&route=TRANS&TemplateID=1507163290651745356&format=JSON'

            response = requests.request("GET",URL)

            return api_response(200, "OTP genereated", [{"OTP":OTP.at(mobile.counter)}], status=True)
        except ObjectDoesNotExist:
            # print(sys.exc_info())
            return api_response(400, "No mobile number found", {}, status=False)
        except:
            # print(sys.exc_info())
            return api_response(400, "OTP generation failed", {}, status=False)

class VerifyOTPView(APIView):

    def post(self, request):
        try:
            mobile = User.objects.get(id = request.data['id'])

            # print(mobile.phone)

            keygen = str(mobile.phone) + str(datetime.date(datetime.now())) + settings.SECRET_KEY
            # print(keygen.returnValue(mobile.phone))

            key = base64.b32encode(keygen.encode())
            OTP = pyotp.HOTP(key)

            if OTP.verify(request.data['otp'], mobile.counter):
                mobile.is_verified_mobile = True
                mobile.save()
                return api_response(200, "you mobile number is verified", {}, status=True)
            else:
                return api_response(400, "Unable to verify mobile", {}, status=False)

    
        except ObjectDoesNotExist:
            # print(sys.exc_info())
            return api_response(400, "No mobile number found", {}, status=False)
        except:
            # print(sys.exc_info())
            return api_response(400, "OTP Verification failed", {}, status=False)
