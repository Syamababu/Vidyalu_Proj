from django.urls import path
from vidyalu_admin.views.admin_views import AdminstudentView,AdminteacherView,AdmincounsellorView,BlockStudentView,BlockTeacherView,BlockCounsellorView,AdminView,AdminverifyteacherView,AdminverifycounsellorView
from vidyalu_admin.views.admin_course_views import AdminCourseDetailsView,AdminBlockCourseView,AdminCourseBookingDetailView,AdminCourseReportGetView
from vidyalu_admin.views.admin_session_views import AdminSessionDetailsView,AdminBlockSessionView,AdminSessionBookingDetailView,AdminsessionReportGetView
from vidyalu_admin.views.support_number_email import SupportNumberEmailView,SupportNumberEmailOnlyView

from vidyalu_admin.views.query_message_view import QueryMessageView,QueryMessageAdminView
from vidyalu_admin.views.category_wise_user import CategoryWiseUser

from vidyalu_admin.views.course_session_category_view import CourseSessionCategoryView, GetCourseSessionCategoryView, DeleteCourseSessionCategoryView
from vidyalu_admin.views.news_letter_email_views import PostNewsLetterEmailView, GetNewsLetterEmailView
from vidyalu_admin.views.competency_areas_views import CompetencyAreasView, CompetencyAreasViewOnly, DeleteCompetencyArea

from vidyalu_admin.views.payment_calculation_views import PaymentCalculationCourseView, PaymentCalculationSessionView


urlpatterns = [
    path("admin/view", AdminView.as_view(), name="admin_profile"),
    path("admin/student", AdminstudentView.as_view(), name="student_details"),
    path("admin/teacher", AdminteacherView.as_view(), name="teacher_details"),
    path("admin/counsellor", AdmincounsellorView.as_view(), name="counsellor_details"),
    # path("admin/block/user", BlockUserView.as_view(), name="block_user_by_id"),
    path("admin/block/student/<int:user_id>", BlockStudentView.as_view(), name="block_user_by_id"),
    path("admin/block/teacher/<int:user_id>", BlockTeacherView.as_view(), name="block_user_by_id"),
    path("admin/block/counsellor/<int:user_id>", BlockCounsellorView.as_view(), name="block_user_by_id"),
    path("admin/teacher/courseall", AdminCourseDetailsView.as_view(), name="course_all"),
    path("admin/counsellor/sessionall", AdminSessionDetailsView.as_view(), name="session_all"),
    path("admin/block/course", AdminBlockCourseView.as_view(), name="block_course"),
    path("admin/block/session", AdminBlockSessionView.as_view(), name="block_session"),
    path("admin/coursebooking/details", AdminCourseBookingDetailView.as_view(), name="course_booking_details"),
    path("admin/sessionbooking/details", AdminSessionBookingDetailView.as_view(), name="session_booking_details"),
    path('support_number_email',SupportNumberEmailView.as_view(), name='support_number_email'),
    path("user_support_number_email",SupportNumberEmailOnlyView.as_view(), name ='user_support_number_email'),
    path('query_message_send', QueryMessageView.as_view(), name='query_message_send'),
    path('get_query_message', QueryMessageAdminView.as_view(), name = 'get_query_message'),
    path('category_wise_user', CategoryWiseUser.as_view(), name='category_wise_user'),
    path('course_session_category',CourseSessionCategoryView.as_view(), name='course_session_category'),
    path('get_course_session_category', GetCourseSessionCategoryView.as_view(), name = 'get_course_session_category'),
    path('delete_course_session_category', DeleteCourseSessionCategoryView.as_view(), name='delete_course_session_category'),
    path('post_news_letter_email',PostNewsLetterEmailView.as_view(), name='post_news_letter_email'),
    path('get_news_letter_email',GetNewsLetterEmailView.as_view(), name='get_news_letter_email' ),
    path('competency_areas', CompetencyAreasView.as_view(), name = 'competency_areas'),
    path('competency_areas_view_only', CompetencyAreasViewOnly.as_view(), name = 'competency_areas_view_only '),
    path('delete_competency', DeleteCompetencyArea.as_view(), name = 'delete_competency'),
    path("admin/get/course/report", AdminCourseReportGetView.as_view(), name="admin_get_course_report"),
    path("admin/get/session/report", AdminsessionReportGetView.as_view(), name="admin_get_session_report"),
    path("admin/verify/teacher", AdminverifyteacherView.as_view(), name="teacher_verify"),
    path("admin/verify/counsellor", AdminverifycounsellorView.as_view(), name="counsellor_verify"),
    path('course_revenue_distribution', PaymentCalculationCourseView.as_view(), name='course_revenue_distribution'),
    path('session_revenue_distribution', PaymentCalculationSessionView.as_view(), name = 'session_revenue_distribution'),



]
