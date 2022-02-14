from rest_framework.serializers import ModelSerializer

from notification.models import SystemNotification


class SystemNotificationSerializer(ModelSerializer):
    class Meta:
        model = SystemNotification
        fields = '__all__'