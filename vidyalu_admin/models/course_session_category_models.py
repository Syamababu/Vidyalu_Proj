from django.db import models

CHOICES = (('course','course'),('session','session'))
class CourseSesssionCategoryModel(models.Model):
    id = models.AutoField(primary_key=True)
    category_type = models.CharField(choices=CHOICES, max_length=100, null=False, blank=False)
    category = models.CharField(max_length=500, null=False, blank=False)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.category