from django.db import models
from core.models.users import User
from counsellor.models.session_model import Session
from django.template.defaultfilters import slugify
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver


class CounsellorTest(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=500, default="session test", null=False, blank=False)
    counsellor = models.ForeignKey(User, on_delete=models.CASCADE)
    session = models.ForeignKey(Session, on_delete=models.CASCADE)
    no_of_question = models.CharField(max_length=200, null=False, blank=False)
    duration = models.CharField(max_length=200, null=False, blank=False)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    total_marks = models.IntegerField(blank=True, null=True)
    active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # deadline = models.DateTimeField(default=now,editable=True,null=False,blank=False)

    class Meta:
        db_table = 'counsellor_tests'

    def __str__(self):
        return self.title