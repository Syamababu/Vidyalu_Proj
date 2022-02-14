from django.urls import path
from core.views.authentication import *
# from core.views.authentication import MyTokenObtainPairView
from rest_framework_simplejwt import views as jwt_views
from core.views.admin_auth import *
# from core.views.role_update import RoleUpdateView
from core.views.search import SearchView

from core.views.teacher_counsellor_rating_review import TeacherCounsellorRatingReview,GetCourseSessionCategoryView

from core.views.admin_auth import AdminUpdatePassword
from core.views.vidyalu_home_view import PopularCourselistView,PopularSessionlistView,PopularTeacherlistView,PopularCounsellorlistView

from core.views.otp_processing_view import GenerateOTPView, VerifyOTPView



urlpatterns = [
    path("api/register", RegisterAPI.as_view(), name="register_user"),
    path("api/login", LoginAPIView.as_view(), name="token_pair"),
    # path("api/user/role/update", RoleUpdateView.as_view(), name="roleupdate"),
    path("api/logout", Logout.as_view(), name="user_logout"),
    # path("token", jwt_views.TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh", jwt_views.TokenRefreshView.as_view(), name="token_refresh"),
    path("api/password/reset", RequestPasswordResetEmail.as_view(), name="password_reset"),
    path("api/password/reset/confirmPasswordReset", SetNewPasswordView.as_view(), name="password_reset_done"),
    path("api/password/change", UpdatePassword.as_view(), name="password_change"),
    path("email-verification", VerifyMyEmailView.as_view(), name="email_verify"),
    # path("api/states", StatesView.as_view(), name="all_states"),
    path("api/location", LocationView.as_view(), name="all_st"),
    path("api/search/list", SearchView.as_view(), name="search_list"),
    path("api/popular/courselist", PopularCourselistView.as_view(), name="popular_courselist"),
    path("api/popular/sessionlist", PopularSessionlistView.as_view(), name="popular_sessionlist"),
    path("api/popular/teacherlist", PopularTeacherlistView.as_view(), name="popular_teacherlist"),
    path("api/popular/counsellorlist", PopularCounsellorlistView.as_view(), name="popular_counsellorlist"),
    path('get/course_session/category', GetCourseSessionCategoryView.as_view(), name='get_course_session_category'),




    # admin urls
    path("api/admin/register", AdminRegisterView.as_view()),
    path("api/admin/login", AdminLoginAPIView.as_view(), name="admin_token"),
    path("api/admin/password/reset", AdminRequestPasswordResetEmail.as_view(), name="password_reset"),
    path("api/admin/password/reset/confirmPasswordReset", AdminSetNewPasswordView.as_view(), name="password_reset_done"),
    path("api/admin/view", AdminView.as_view(), name="admin_profile"),
    path("api/teacher_counsellor_rating_review", TeacherCounsellorRatingReview.as_view(),name='teacher_counsellor_rating_review'),
    path("api/admin/admin_update_password", AdminUpdatePassword.as_view(), name='admin_update_password'),

    path('api/generate_otp',GenerateOTPView.as_view(), name = 'generate_otp'),
    path('api/verify_otp',VerifyOTPView.as_view(), name = 'verify_otp'),


    # path("admin/password/change", UpdatePassword.as_view(), name="password_change"),


]
