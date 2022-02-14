from django.urls import path

from notification.views.get_notifications import GetNotification

urlpatterns = [
    path('get_notification', GetNotification.as_view(), name = 'get_notification'),
    ]