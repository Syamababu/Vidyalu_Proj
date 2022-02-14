from rest_framework.views import APIView

from vidyalu_admin.models.support_number_email import SupportNumberEmail

from vidyalu_admin.serializers.support_number_email_serializer import SupportNumberEmailSerializer

from core.permissions import IsAdmin, IsStudentTeacherCounsellor

from core.helpers import api_response
import sys

class SupportNumberEmailView(APIView):
    permission_classes = (IsAdmin,)

    def get(self, request):
        try:
            number_email = SupportNumberEmail.objects.get(id = 1)
            serializer = SupportNumberEmailSerializer(number_email)
            return api_response(200, "Support number and email fetched", [serializer.data], status= True)
        except:
            return api_response(200, "Support number and email fetching failed", {},status= True)


    def put(self, request):
        try:
            number_email = SupportNumberEmail.objects.get(id = 1)
            serializer = SupportNumberEmailSerializer(data = request.data, instance=number_email, partial = True)
            if serializer.is_valid():
                serializer.save()
                return api_response(200, "Support number and email update succeessfully", [serializer.data], status=True)
        except:
            request.POST.__mutable = True
            SupportNumberEmail.objects.create(id = 1, email = request.data['email'], number = request.data['number'])
            number_email = SupportNumberEmail.objects.get(id = 1)
            request.POST.__mutable = False
            serializer = SupportNumberEmailSerializer(number_email)
            return api_response(200, "Support number and email update succeessfully", [serializer.data], status=True)
            # except:
            #     print(sys.exc_info())
            #     return api_response(400, "Support number and email update failed", {}, status=False)

class SupportNumberEmailOnlyView(APIView):
    # permission_classes = (IsStudentTeacherCounsellor,)

    def get(self, request):
        try:
            number_email = SupportNumberEmail.objects.get(id = 1)
            serializer = SupportNumberEmailSerializer(number_email)
            return api_response(200, "Support number and email fetched", [serializer.data], status= True)
        except:
            return api_response(200, "Support number and email fetching failed",{}, status= True)

