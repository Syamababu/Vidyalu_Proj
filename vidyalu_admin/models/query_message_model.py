from django.db import models

class QueryMessageModel(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=500, null=False, blank=False, default="NAME")
    email = models.EmailField(default="querymail@mail.com", null=False, blank=False)
    number = models.CharField(default="0000000000", max_length=100, null=False, blank=False)
    message = models.TextField(default="Query message",null=False, blank=False)

    def __str__(self):
        return str(self.id)
