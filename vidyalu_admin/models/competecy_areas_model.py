from django.db import models

class CompetencyAreasModel(models.Model):
    id = models.AutoField(primary_key=True)
    competency_area = models.CharField(max_length=250, null=False, blank=False)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return str(self.id)