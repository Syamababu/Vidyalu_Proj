from django.db import models
from core.models.users import User
from counsellor.models.session_model import Session


class SessionReport(models.Model):
    """
            Student Session Report model.
    """
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name='student_sessionreport_user',null=True)
    counsellor = models.ForeignKey(User, on_delete=models.CASCADE,related_name='counsellor_report_user',null=True)
    session = models.ForeignKey(Session, on_delete=models.CASCADE,null=True)
    report = models.CharField(max_length=5000,null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    class Meta:
        db_table = "session_report"
        verbose_name = "Session_report"
        verbose_name_plural = "Session_report"


