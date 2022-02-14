from django.db import models

class SupportNumberEmail(models.Model):
    id = models.AutoField(primary_key=True)
    # country_code = models.CharField(default='+91',max_length=10, null=False, blank=False)
    number = models.IntegerField(default=00000000000, null=False, blank=False)
    email = models.EmailField(default="vidyalu.help@mailinator.com", null=False, blank=False)


    def __str__(self):
        return str(self.id)