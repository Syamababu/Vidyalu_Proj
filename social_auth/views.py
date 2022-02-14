from core.models.users import User
from rest_framework.views import APIView
from core.helpers import api_response
from social_auth.serializers import GoogleUserSerializer
from social_auth.models import SocialAccount
from urllib.parse import urlparse
import requests
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from student.models.students import Student
from teacher.models.teachers import Teacher
from counsellor.models.counsellors import Counsellor
from core.serializers.auth_serializer import MyTokenObtainPairSerializer


def do_login(request, email, password):
    data = {"email": email, "password": password}
    print(data)
    # def post(request):
    serializer = MyTokenObtainPairSerializer(data=data)
    print(serializer)
    if serializer.is_valid():
        return api_response(200, "Login success", serializer.data["tokens"], status=True)
    else:
        errors_list = [serializer.errors[error][0] for error in serializer.errors]
        return api_response(400, errors_list[0], {}, status=False)


class GoogleSocialAuthView(APIView):
    def post(self, request):
        email = request.data["email"]
        if User.objects.filter(email=email).exists():
            user = User.objects.get(email=email)
            serializer = GoogleUserSerializer(user, data=request.data)
            if serializer.is_valid():
                serializer.save()
                userid = serializer.data.get("id", None)
                provider = request.data.get("provider", None)
                extra_data = request.data
                auth_token = request.data.get("auth_token", None)
                id_token = request.data.get("id_token", None)
                google_id = request.data.get("id", None)
                acc = SocialAccount.objects.get(user_id=user.id)
                acc.user_id = userid
                acc.provider = provider
                acc.extra_data = extra_data
                acc.auth_token = auth_token
                acc.id_token = id_token
                acc.uid = google_id
                acc.save()
            resp = do_login(request, email, request.data["T_password"])
            return resp
            # return api_response(200, "social login user updated successfully.",{"email": email, "password": request.data["T_password"]}, status=True)
        else:
            serializer = GoogleUserSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                userid = serializer.data.get("id", None)
                provider = request.data.get("provider", None)
                extra_data = request.data
                auth_token = request.data.get("auth_token", None)
                id_token = request.data.get("id_token", None)
                google_id = request.data.get("id", None)
                social_user = SocialAccount.objects.create(
                    user_id=userid,
                    provider=provider,
                    extra_data=extra_data,
                    auth_token=auth_token,
                    id_token=id_token,
                    uid=google_id,
                )
            resp = do_login(request, email, request.data["T_password"])
            return resp

# class ChangeroleStataus(APIView):
#     permission_classes = (IsAuthenticated,)
#
#     def put(self,request):
#         role = request.data.get("role", "")
#         if SocialAccount.objects.filter(user_id=request.user.id).exists():
#             acc = SocialAccount.objects.get(user_id=request.user.id)
#             user = acc.user_id
#             usr = User.objects.get(id=user)
#             if role == "student":
#                 usr.is_student = True
#                 Student.objects.create(student=usr)
#             if role == "teacher":
#                 usr.is_teacher = True
#                 Teacher.objects.create(teacher=usr)
#             if role == "counsellor":
#                 usr.is_counsellor = True
#                 Counsellor.objects.create(counsellor=usr)
#             else:
#                 role = ""
#             usr.save()
#
#             return api_response(200, "role updated", {"role": role}, status=True)
#         else:
#             return api_response(400, "User Not Found", {}, status=False)

class ChangeroleStataus(APIView):
    permission_classes = (IsAuthenticated,)

    def put(self,request):
        role = request.data["role"]
        if SocialAccount.objects.filter(user_id=request.user.id).exists():
            acc = SocialAccount.objects.get(user_id=request.user.id)
            user = acc.user_id
            usr = User.objects.get(id=user)
            usr.role = role
            usr.save()
            if usr.role == "student":
                Student.objects.create(student=usr)
            elif usr.role == "teacher":
                Teacher.objects.create(teacher=usr,permission_by_admin=False)
            elif usr.role == "counsellor":
                Counsellor.objects.create(counsellor=usr,permission_by_admin=False)
            if usr.role == None:
                role = ""
            else:
                role = usr.role
            return api_response(200, "role updated", {"role": role}, status=True)
        else:
            return api_response(400, "User Not Found", {}, status=False)


# class ChangeroleStataus(APIView):
#     def put(self, request, auth_token=None):
#         auth_token = request.data.get("auth_token", auth_token)
#         role = request.data.get("role", None)
#         if SocialAccount.objects.filter(auth_token=auth_token).exists():
#             acc = SocialAccount.objects.get(auth_token = auth_token)
#             user = acc.user_id
#             usr = User.objects.get(id=user)
#             usr.role = role
#             usr.save()
#
            # if usr.role == "student":
            #     Student.objects.create(student=usr)
            # elif usr.role == "teacher":
            #     Teacher.objects.create(teacher=usr)
            # elif usr.role == "counsellor":
            #     Counsellor.objects.create(counsellor=usr)
#             # if user.role == "student":
#
        #     if usr.role == None:
        #         role = ""
        #     else:
        #         role = usr.role
        #     return api_response(200, "role updated", {"role": role}, status=True)
        # else:
        #     return api_response(400, "User Not Found", {}, status=False)

# class ChangeroleStataus(APIView):
#     def put(self, request, email=None):
#         email = request.data.get("email", email)
#         role = request.data.get("role", None)
#         try:
#             user = User.objects.get(email=email)
#             user.role = role
#             user.save()
#             if user.role == None:
#                 role = ""
#             elif user.role == user.role:
#                 role = user.role
#             return api_response(200, "role updated", {"role": role})
#         except User.DoesNotExist:
#             return api_response(400, "User Not Found", {}, status=False)
