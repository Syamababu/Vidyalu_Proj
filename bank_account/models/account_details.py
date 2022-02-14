from django.db import models

from core.models.users import User

class AccountDetails(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bank_name = models.CharField(default='bank name', max_length=500, null=False, blank=False)
    branch_name = models.CharField(default='branch name', max_length=500, null= False, blank=False)
    account_holder_name = models.CharField(default='account holder name',max_length=600, null=False, blank= False)
    account_number = models.CharField(default='000000000000', max_length = 250,  null=False, blank=False)
    ifsc_code = models.CharField(default='ifsc code', max_length=250, null=False, blank=False)

    def __str__(self):
        return str(self.id)

    class Meta:
        db_table = 'bank_account_details'