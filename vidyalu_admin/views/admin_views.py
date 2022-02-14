from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from core.helpers import api_response
from student.models.students import Student
from teacher.models.teachers import Teacher
from counsellor.models.counsellors import Counsellor
from vidyalu_admin.serializers.admin_serializer import StudentSerializer,TeacherSerializer,CounsellorSerializer,UserSerializer,AdminverifyteacherSerializer,AdminverifycounsellorSerializer
from core.models.users import User
from rest_framework.parsers import FileUploadParser
from core.views.send_emails import send_onboard_userverify,send_board_userverify



class AdminstudentView(APIView):
    permission_classes = (IsAdminUser,)

    def get(self, request):
        student = Student.objects.all().order_by('-created_at')
        if student:
            serializer = StudentSerializer(student, many=True)
            return api_response(200, "Student profile retrieved successfully.", serializer.data, status=True)
        else:
            return  api_response(404,"No students found",{},status=False)


class AdminteacherView(APIView):
    permission_classes = (IsAdminUser,)

    def get(self,request):
        teacher = Teacher.objects.all().order_by('-created_at')
        if teacher:
            serializer =TeacherSerializer(teacher, many=True)
            serializer_data = sorted(serializer.data, key = lambda k:k['report_count'], reverse = True)
            return api_response(200, "Teacher profile retrieved successfully.", serializer_data, status=True)
        else:
            return api_response(404, "No teachers found", {}, status=False)


class AdmincounsellorView(APIView):
    permission_classes = (IsAdminUser,)


    def get(self,request):
        counsellor = Counsellor.objects.all().order_by('-created_at')
        if counsellor:
            serializer = CounsellorSerializer(counsellor, many=True)
            serializer_data = sorted(serializer.data, key = lambda k:k['report_count'], reverse = True)
            return api_response(200, "Counsellor profile retrieved successfully.", serializer_data, status=True)
        else:
            return api_response(404, "No counsellor found", {}, status=False)



# class BlockUserView(APIView):
#     # permission_classes = (IsAdminUser,)
#
#
#     def put(self,request):
#         try:
#             user_id=request.data.get("id",None)
#             print(user_id)
#             user = User.objects.get(id=user_id)
#             serializer = blockbyadminSerializer(user,data=request.data)
#             if serializer.is_valid():
#                 serializer.save()
#                 return api_response(200, "unblocked by admin  successfully", {}, status=False)
#             else:
#                 return api_response(200, "unblocked by admin  successfully", {}, status=False)
#         except User.DoesNotExist:
#             return api_response(400, "User Not Found", {}, status=False)



class BlockStudentView(APIView):
    permission_classes = (IsAdminUser,)

    def put(self,request,user_id):
        try:
            user = User.objects.get(id=user_id)
            if user.block_by_admin == False:
                user.block_by_admin = True
                user.save()
                return api_response(200, "Blocked by admin  successfully", request.data, status=True)
            elif user.block_by_admin == True:
                user.block_by_admin = False
                user.save()
                return api_response(200, "Unblocked by admin  successfully", {}, status=True)
        except User.DoesNotExist:
            return api_response(400, "User Not Found", {}, status=False)


class BlockTeacherView(APIView):
    permission_classes = (IsAdminUser,)

    def put(self,request,user_id):
        try:
            user = User.objects.get(id=user_id)
            if user.block_by_admin == False:
                user.block_by_admin = True
                user.save()
                return api_response(200, "Blocked by admin  successfully", request.data, status=True)
            elif user.block_by_admin == True:
                user.block_by_admin = False
                user.save()
                return api_response(200, "Unblocked by admin  successfully", {}, status=True)
        except User.DoesNotExist:
            return api_response(400, "User Not Found", {}, status=False)


class BlockCounsellorView(APIView):
    permission_classes = (IsAdminUser,)

    def put(self,request,user_id):
        try:
            user = User.objects.get(id=user_id)
            if user.block_by_admin == False:
                user.block_by_admin = True
                user.save()
                return api_response(200, "Blocked by admin  successfully", request.data, status=True)
            elif user.block_by_admin == True:
                user.block_by_admin = False
                user.save()
                return api_response(200, "Unblocked by admin  successfully", {}, status=True)
        except User.DoesNotExist:
            return api_response(400, "User Not Found", {}, status=False)


class AdminView(APIView):
    permission_classes = (IsAdminUser,)
    # parser_class = (FileUploadParser,)

    def get(self,request):
        try:
            user = User.objects.get(id=request.user.id)
            serializer = UserSerializer(user)
            print("hello")
            return api_response(200, "Admin profile retrieved successfully.", serializer.data, status=True)
        except User.DoesNotExist:
            return api_response(400, "Admin Not Found", {}, status=False)

    # def put(self, request):
    #
    #     try:
    #
    #         user = User.objects.get(id=request.user.id)
    #         if "email" in request.data:
    #             user.email = request.data["email"]
    #         if "username" in request.data:
    #             user.username = request.data["username"]
    #         if "profile_image" in request.data:
    #             user.profile_image = request.data["profile_image"]
    #         user.save()
    #         return api_response(200, "Profile updated successfully", request.data, status=True)
    #
    #     except User.DoesNotExist:
    #         return api_response(400, "Admin Not Found", {}, status=False)

    def put(self,request):
        try:
            user = User.objects.get(id=request.user.id)
            serializer = UserSerializer(user, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return api_response(200, "Profile updated successfully", request.data, status=True)
            else:
                return api_response(400, "Invalid data", {}, status=False)
        except User.DoesNotExist:
            return api_response(400, "Admin Not Found", {}, status=False)


class AdminUpdatePassword(APIView):
    """
    An endpoint for reset password.
    """

    permission_classes = (IsAuthenticated,)

    def get_object(self, queryset=None):
        return self.request.user

    def put(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = ChangePasswordSerializer(data=request.data)

        if serializer.is_valid():
            # Check old password
            old_password = serializer.data.get("old_password")
            if not self.object.check_password(old_password):
                return api_response(400, "Wrong old_password.", {}, status=False)
            # set_password also hashes the password that the user will get
            self.object.set_password(serializer.data.get("new_password"))
            self.object.save()
            return api_response(200, "password updated successfully", {}, status=True)
        else:
            errors_list = [serializer.errors[error][0] for error in serializer.errors]
            return api_response(400, errors_list[0], {}, status=False)

        # return api_response(400, "password not updated.", {}, status=False)



class AdminverifyteacherView(APIView):
    """
            Admin can block student user.
    """
    permission_classes = (IsAdminUser,)

    def put(self,request):
        try:
            user_id = request.data.get("id", None)
            admn_cmt = request.data.get("admin_comment", None)
            admn_per = request.data.get("permission_by_admin", None)
            print(admn_cmt)
            u_email= User.objects.get(id=user_id)
            user = Teacher.objects.get(teacher_id=user_id)
            print(u_email.email)
            serializer = AdminverifyteacherSerializer(user, data=request.data, partial=True)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                # send_onboard_userverify(request, u_email.email,admn_cmt)
                send_board_userverify(request, u_email.email,admn_cmt,admn_per)
                return api_response(200, "verify Updated successfully", serializer.data, status=True)
            else:
                return api_response(400, "Invalid data", {}, status=False)
        except Teacher.DoesNotExist:
            return api_response(400, "User Not Found", {}, status=False)





class AdminverifycounsellorView(APIView):
    """
            Admin can block student user.
    """
    permission_classes = (IsAdminUser,)

    def put(self, request):
        try:
            user_id = request.data.get("id", None)
            admn_cmt = request.data.get("admin_comment", None)
            admn_per = request.data.get("permission_by_admin", None)
            print(admn_cmt)
            u_email = User.objects.get(id=user_id)
            user = Counsellor.objects.get(counsellor_id=user_id)
            print(u_email.email)
            serializer = AdminverifycounsellorSerializer(user, data=request.data, partial=True)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                # send_onboard_userverify(request, u_email.email, admn_cmt)
                send_board_userverify(request, u_email.email,admn_cmt,admn_per)
                return api_response(200, "verify Updated successfully", serializer.data, status=True)
            else:
                return api_response(400, "Invalid data", {}, status=False)
        except Counsellor.DoesNotExist:
            return api_response(400, "User Not Found", {}, status=False)