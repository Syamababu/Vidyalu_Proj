from django.urls import path

from bank_account.views.bank_account_details import BankAccountView

urlpatterns = [
    path('bank_account_details',BankAccountView.as_view(), name = 'bank_account_details'),
]