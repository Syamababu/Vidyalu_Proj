from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

from notification.models import SystemNotification

from notification.serializers.system_notification_serializers import SystemNotificationSerializer

from core.helpers import api_response


class GetNotification(APIView):
    permission_class = (IsAuthenticated,)

    def get(self, request):
        user = self.request.user
        notifications = SystemNotification.objects.filter(user = user).order_by('-id')
        serializer = SystemNotificationSerializer(notifications, many = True)

        return api_response(200,"notifications retrived successfully", serializer.data, status=True)