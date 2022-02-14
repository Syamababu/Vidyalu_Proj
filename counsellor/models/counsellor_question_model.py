from django.db import models
from counsellor.models.counsellor_test_model import CounsellorTest
from counsellor.models.session_model import Session
from core.models.users import User


class CounsellorQuestion(models.Model):
    id = models.AutoField(primary_key=True)
    test = models.ForeignKey(CounsellorTest, on_delete=models.CASCADE)
    session = models.ForeignKey(Session, on_delete=models.CASCADE)
    counsellor = models.ForeignKey(User, on_delete=models.CASCADE)
    question_text = models.CharField(max_length=1000, null=True, blank=True)
    option = models.JSONField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # score = models.IntegerField(null=True,blank=True)

    class Meta:
        db_table = "counsellor_questions"

    def __str__(self):
        return self.question_text