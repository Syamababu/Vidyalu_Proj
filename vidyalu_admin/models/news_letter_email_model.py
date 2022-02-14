from django.db import models


class NewsLetterEmailModel(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.EmailField(null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return str(self.id)

    class Meta:
        db_table = 'newsletteremail'