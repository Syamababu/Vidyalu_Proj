from django.db import models
from core.models.users import User
from counsellor.models.session_model import Session
from counsellor.models.counsellor_test_model import CounsellorTest
from counsellor.models.counsellor_question_model import CounsellorQuestion


class SessionTestResult(models.Model):
    id = models.AutoField(primary_key=True)
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    # course = models.ForeignKey(Course, on_delete=models.CASCADE)
    test = models.ForeignKey(CounsellorTest, on_delete=models.CASCADE)
    total_mark = models.IntegerField(blank=True,null=True)
    score = models.IntegerField(default=0,blank=True,null=True)
    no_of_skip = models.IntegerField(default=0,blank=True,null=True)
    no_of_attempt = models.IntegerField(default=0,blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # deadline = models.DateTimeField(default=now,editable=True,null=False,blank=False)

    class Meta:
        db_table = 'student_sessiontest_result'

    # @property
    # def score(self):
    #     if self.question:
    #         qtn=self.question
    #         return len(list(filter(lambda ans:ans["is_correct"]==True,qtn)))
