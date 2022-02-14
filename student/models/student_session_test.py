from django.db import models
from core.models.users import User
from counsellor.models.session_model import Session
from counsellor.models.counsellor_test_model import CounsellorTest
from counsellor.models.counsellor_question_model import CounsellorQuestion


class StudentSessionTest(models.Model):
    id = models.AutoField(primary_key=True)
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    session = models.ForeignKey(Session, on_delete=models.CASCADE)
    test = models.ForeignKey(CounsellorTest, on_delete=models.CASCADE)
    question = models.JSONField(null=True, blank=True)
    score = models.IntegerField(default=0)
    test_attempt = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # deadline = models.DateTimeField(default=now,editable=True,null=False,blank=False)

    class Meta:
        db_table = 'student_session_test'

    # @property
    # def score(self):
    #     if self.question:
    #         qtn=self.question
    #         return len(list(filter(lambda ans:ans["is_correct"]==True,qtn)))
