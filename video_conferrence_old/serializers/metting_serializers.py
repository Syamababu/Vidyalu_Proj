
from rest_framework import serializers
from video_conferrence.models.zoom_meeting_model import ZoomMeetingCreate




class ZoommettingSerializer(serializers.ModelSerializer):
    class Meta:
        model = ZoomMeetingCreate
        fields = "__all__"
