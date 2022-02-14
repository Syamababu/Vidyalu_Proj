from django.urls import path
from counsellor.views.counsellor_detail import CounsellorView,CounsellorBasicinformation,CounsellorApplicationform,CounsellorUploaddoc
from counsellor.views.session_detail import SessionAPIView,SessionDetailView,SessionEditView,PublishSessionView,CounsellorSessionBookingDetailView,counsellorCountSessionView,ActiveSessionDetailView
from counsellor.views.session_schedule import SessionScheduleView
from video_conference.views.conference_details_view import CreateConferenceURL
from counsellor.views.get_student_chat_list import StudentChatList
from counsellor.views.counsellor_test_details import CounsellorCreatTestView,CounsellorGetTestView,CounsellorPutTestView,ActiveSessionTestView,CounsellorGetStudentDetailView,CounsellorGetStudentTestResultView
from counsellor.views.counsellor_questions_details import CounsellorTestQuestionAPI,CounsellorTestGetQuestionAPI,CounsellorTestChangeQuestionAPI,CounsellorTestDeleteQuestionAPI
from counsellor.views.student_count_view import CounsellorCountStudentView

urlpatterns = [
    path("counsellor", CounsellorView.as_view(), name="counsellor_profile"),
    path("counsellor/basicinfo", CounsellorBasicinformation.as_view(), name="teacher_basicinformation"),
    path("counsellor/appform", CounsellorApplicationform.as_view(), name="counsellor_applicationform"),
    path("counsellor/uploaddoc", CounsellorUploaddoc.as_view(), name="counsellor_uploaddoc"),
    path("counsellor/session", SessionAPIView.as_view(), name="counsellor_session"),
    path("counsellor/sessionall", SessionDetailView.as_view(), name="session_all"),
    path("counsellor/session/edit", SessionEditView.as_view(), name="session_edit"),
    path("counsellor/session/publish", PublishSessionView.as_view(), name="publish_session"),
    path("counsellor/session/booking/details", CounsellorSessionBookingDetailView.as_view(), name="session_booking_details"),
    path("counsellor/get_class_list", SessionScheduleView.as_view(), name="session_schedule_view"),
    path('counsellor/create_meeting_url', CreateConferenceURL.as_view(), name='create_meeting_url'),
    path("counsellor/get_student_chat_list",StudentChatList.as_view(), name="get_student_chat_list"),
    path('counsellor/test', CounsellorCreatTestView.as_view(), name="create_test"),
    path('counsellor/testdetails', CounsellorGetTestView.as_view(), name="get_testdetails"),
    path('counsellor/change/testdetails', CounsellorPutTestView.as_view(), name="change_testdetails"),
    path("counsellor/test/active", ActiveSessionTestView.as_view(), name="active_test"),
    path('counsellor/test_question', CounsellorTestQuestionAPI.as_view(), name="test_question"),
    path('counsellor/get/test_question', CounsellorTestGetQuestionAPI.as_view(), name="get_question"),
    path('counsellor/change/test_question', CounsellorTestChangeQuestionAPI.as_view(), name="change_question"),
    path('counsellor/delete/test_question', CounsellorTestDeleteQuestionAPI.as_view(), name="delete_question"),
    path('counsellor/count/student', CounsellorCountStudentView.as_view(),name="student_count"),
    path('counsellor/count/session', counsellorCountSessionView.as_view(),name="session_count"),
    path('counsellor/count/session_detail', ActiveSessionDetailView.as_view(),name="session_count_details"),
    path("counsellor/test/student/details", CounsellorGetStudentDetailView.as_view(), name="counsellor_test_student_details"),
    path("counsellor/student/test/result", CounsellorGetStudentTestResultView.as_view(), name="counsellor_test_student_result"),

    # path("counsellor/all/sessionbooking/details", TeacherAllCourseBookingDetailView.as_view(),name="course_booking_details_all"),
]
