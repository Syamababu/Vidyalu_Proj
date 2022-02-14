from django.urls import path

from video_conferrence.views.meeting_view import CreateMeetingURL,CreateZoomMeetingURL


urlpatterns = [
    path('create_meeting_url',CreateMeetingURL.as_view(),name = 'create_meeting_url'),
    path('create/zoom/meeting_url',CreateZoomMeetingURL.as_view(),name = 'create_meeting_url'),

]