from django.db import models
from core.models.users import User
from counsellor.models.session_model import Session


class SessionRating(models.Model):
    """
            Student Session Rating model.
    """
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name='student_sessionrateing_user',null=True)
    counsellor = models.ForeignKey(User, on_delete=models.CASCADE,related_name='counsellor_rating_user',null=True)
    session = models.ForeignKey(Session, on_delete=models.CASCADE,null=True)
    review = models.CharField(max_length=5000, null=True, blank=True)
    rating = models.IntegerField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    class Meta:
        db_table = "session_rating"
        verbose_name = "Session_rating"
        verbose_name_plural = "Session_rating"


