from django.urls import path
from student.views.student_detail import StudentView,StudentBasicinformation,StudentcounsellorView
from student.views.student_course_views import StudentCourseallView,StudentCourseDetailsView,TeacherCourseDetailView, StudentCourseDetailsOnlyView
from student.views.student_session_views import StudentSessionallView,StudentSessionDetailsView,CounsellorSessionDetailView, StudentSessionDetailsOnlyView
from student.views.course_booking_views import StudentCourseBookingView,StudentCourseBookingDetailView
from student.views.session_booking_views import StudentSessionBookingView,StudentSessionBookingDetailView
from student.views.past_live_upcoming_course_view import PastLiveUpcomingCourseView
from student.views.past_life_upcoming_session_view import PastLiveUpcomingSessionView
from student.views.course_schedule_view import StudentCourseScheduleView
from student.views.get_class import LatestClass
from student.views.teacher_list_view import TeacherlistView
from student.views.student_question_views import StudentQuestionView
from student.views.student_question_views import StudentTestView
from student.views.student_test_views import StudentGetTestdetailView,ActiveStudentTestView,StudentTestResultView
from student.views.session_schedule_view import StudentSessionScheduleView
from student.views.get_teacher_chat_list import TeacherChatList
from student.views.get_counsellor_chat_list import CounsellorChatList
from student.views.get_session import LatestSession
from student.views.student_sessiontest_view import StudentSessionTestdetailView,ActiveStudentSessionTestView,StudentSessionTestResultView
from student.views.student_session_question import StudentSessionQuestionView,StudentSessionTestAnswerView
from student.views.student_dashboard_view import StudentRunningPastCoursesView,StudentRunningPastSessionsView,StudentPopularCourseView,StudentPopularSessionView
from student.views.course_rating_view import StudentCourseRatingView,StudentCourseRatingEditView,StudentCourseRatingGetView,StudentCourseReviewGetView
from student.views.session_rating_view import StudentSessionRatingView,StudentSessionRatingEditView,StudentSessionRatingGetView,StudentSessionReviewGetView

from student.views.get_course_session_category import CourseSessionCategoryViewOnly
from student.views.course_report_view import StudentCourseReportView,StudentCourseReportGetView,StudentCourseReportEditView
from student.views.session_report_view import StudentSessionReportView,StudentSessionReportGetView,StudentSessionReportEditView


urlpatterns = [
    path("student", StudentView.as_view(), name="student_profile"),
    path("student/basicinfo", StudentBasicinformation.as_view(), name="student_basicinformation"),
    path("student/counsellor", StudentcounsellorView.as_view(), name="counsellor_details"),
    path("student/courseall", StudentCourseallView.as_view(), name="course_all_details"),
    path("student/sessionall", StudentSessionallView.as_view(), name="session_all_details"),
    path("student/course/details", StudentCourseDetailsView.as_view(), name="course_details"),
    path("student/course/details_only",StudentCourseDetailsOnlyView.as_view(), name = "course_details_only"),
    path("student/session/details", StudentSessionDetailsView.as_view(), name="session_details"),
    path("student/session/details_only", StudentSessionDetailsOnlyView.as_view(), name="session_details_only"),
    path("search/teacher/course", TeacherCourseDetailView.as_view(), name="teacher_course"),
    path("search/counsellor/session", CounsellorSessionDetailView.as_view(), name="counsellor_session"),
    path("student/course/booking", StudentCourseBookingView.as_view(), name="course_booking"),
    path("student/course/booking/details", StudentCourseBookingDetailView.as_view(), name="course_booking_detail"),
    path("student/session/booking", StudentSessionBookingView.as_view(), name="session_booking"),
    path("student/session/booking/details", StudentSessionBookingDetailView.as_view(), name="session_booking_detail"),
    path("student/past_live_upcoming_course",PastLiveUpcomingCourseView.as_view(), name="past_live_upcoming_course"),
    path("student/past_live_upcoming_session",PastLiveUpcomingSessionView.as_view(),name="past_live_upcoming_session"),
    path("student/get_class_list", StudentCourseScheduleView.as_view(), name="course_schedule_view"),
    path("student/get_class",LatestClass.as_view(),name="get_class"),
    path("student/get_teacher_list", TeacherlistView.as_view(), name="teacher_list_view"),
    path("student/get_question/list", StudentQuestionView.as_view(), name='get_test_question'),
    path("student/test_view", StudentTestView.as_view(), name='student_test'),
    path('student/testdetails/list', StudentGetTestdetailView.as_view(), name='student_testdetails'),
    path("student/test/active", ActiveStudentTestView.as_view(), name="active_test_student"),
    path("student/test/result", StudentTestResultView.as_view(), name="test_result"),
    path("student/get_session_list", StudentSessionScheduleView.as_view(), name="session_schedule_view"),
    path('student/get_teacher_chat_list',TeacherChatList.as_view(), name='get_teacher_chat_list'),
    path('student/get_counsellor_chat_list',CounsellorChatList.as_view(),name='counsellor_chat_list'),
    path("student/get_session", LatestSession.as_view(), name="get_session"),
    path('student/sessiontest/list', StudentSessionTestdetailView.as_view(), name='student_sessiontest_details'),
    path("student/session_question/list", StudentSessionQuestionView.as_view(), name='session_test_question'),
    path("student/sessiontest/answer", StudentSessionTestAnswerView.as_view(), name='student_sessiontest_answer'),
    path("student/sessiontest/active", ActiveStudentSessionTestView.as_view(), name="active_sessiontest_student"),
    path("student/sessiontest/result", StudentSessionTestResultView.as_view(), name="session_test_result"),
    path("student/running_past/courses", StudentRunningPastCoursesView.as_view(), name="student_running_courses"),
    path("student/running_past/sessions", StudentRunningPastSessionsView.as_view(), name="student_past_sessions"),
    path("student/popular/courselist", StudentPopularCourseView.as_view(), name="student_popular_course"),
    path("student/popular/sessionlist", StudentPopularSessionView.as_view(), name="student_popular_session"),
    path("student/course/rating", StudentCourseRatingView.as_view(), name="student_course_rating"),
    path("student/update/course/rating", StudentCourseRatingEditView.as_view(), name="student_update_rating"),
    path("student/get/course/rating", StudentCourseRatingGetView.as_view(), name="student_get_rating"),
    path("student/session/rating", StudentSessionRatingView.as_view(), name="student_session_rating"),
    path("student/update/session/rating", StudentSessionRatingEditView.as_view(), name="student_update_session_rating"),
    path("student/get/session/rating", StudentSessionRatingGetView.as_view(), name="student_get_session_rating"),
    path("student/get/course/review", StudentCourseReviewGetView.as_view(), name="student_get_review"),
    path("student/get/session/review", StudentSessionReviewGetView.as_view(), name="student_get_session_review"),
    path('get_course_session_category_view_only', CourseSessionCategoryViewOnly.as_view(), name='get_course_session_category_view_only'),
    path("student/course/report", StudentCourseReportView.as_view(), name="student_course_report"),
    path("student/get/course/report", StudentCourseReportGetView.as_view(), name="student_getcourse_report"),
    path("student/session/report", StudentSessionReportView.as_view(), name="student_session_report"),
    path("student/get/session/report", StudentSessionReportGetView.as_view(), name="student_getsession_report"),
    path("student/update/course/report", StudentCourseReportEditView.as_view(), name="student_update_report"),
    path("student/update/session/report", StudentSessionReportEditView.as_view(), name="student_update_session_report"),


    # path("search/teacher/Profile", TeacherProfileDetailView.as_view(), name="teacher_profile"),
    # path("search/counsellor/Profile", CounsellorProfileDetailView.as_view(), name="counsellor_profile"),
    # path("search/teacher/course/details", SearchTeacherCourseDetailsView.as_view(), name="teacher_course"),
    # path("search/counsellor/session/details", SearchCounsellorSessionDetailsView.as_view(), name="counsellor_session"),

]
