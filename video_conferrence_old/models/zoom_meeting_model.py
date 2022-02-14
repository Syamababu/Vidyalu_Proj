from django.db import models


class ZoomMeetingCreate(models.Model):
    meeting_url = models.CharField(max_length=199, default="")
    meeting_password = models.CharField(max_length=199, null=True, blank=True)
    meeting_topic = models.CharField(max_length=199, null=True, blank=True)
    meeting_time = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = "zoommeetingcreate"
