from django.contrib import admin

from notification.models import Notification, SystemNotification

# Register your models here.

admin.site.register(Notification)
admin.site.register(SystemNotification)