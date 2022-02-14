from rest_framework.views import APIView

from core.permissions import IsTeacherCounsellor
from core.helpers import api_response

from bank_account.models.account_details import AccountDetails

from bank_account.serializers.bank_account_details_serializers import BankAccountSerializer

class BankAccountView(APIView):
    permission_classes = (IsTeacherCounsellor,)

    def get(self, request):
        try:
            user = self.request.user
            account_details = AccountDetails.objects.get(user = user)
            serializer = BankAccountSerializer(account_details)
            return api_response(200, "account details fetched", [serializer.data], status=True)
        except:
            return api_response(400, "no account found of this user", {}, status=False)


    def post(self, request):
        user = self.request.user
        request.POST.__mutable = True

        account_holder_names = request.data['account_holder_name'].split(' ')

        for i in account_holder_names:
            if i.isalpha():
                pass
            else:
                return api_response(400, "account update failed. account holder name contains other than alpha character", {}, status=False)

        request.data['account_holder_name']= request.data['account_holder_name'].upper()
        
        request.data['user'] = user.id

        request.POST.__mutable = False

        serializer = BankAccountSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return api_response(200, "account updated succesfully", [serializer.data], status=True)

        return api_response(400, "account update failed", [serializer.errors], status=False)

    def put(self, request):

        user = self.request.user
        # request.POST.__mutable = True

        account_holder_names = request.data['account_holder_name'].split(' ')

        for i in account_holder_names:
            if i.isalpha():
                pass
            else:
                return api_response(400, "account update failed. account holder name contains other than alpha character", {}, status=False)

        request.data['account_holder_name']= request.data['account_holder_name'].upper()

        account_details = AccountDetails.objects.get(user = user)

        # request.data['user'] = user.id
        serializer = BankAccountSerializer(instance=account_details, data = request.data,partial = True)
        
        if serializer.is_valid():
            serializer.save()
            return api_response(200, "account updated succesfully", [serializer.data], status=True)
        
        return api_response(400, "account update failed", {}, status=False)

    def delete(self, request):
        user = self.request.user

        try:
            account = AccountDetails.objects.get(user = user)
            account.delete()
            return api_response(200,"account successfully deleted", {}, status=True)
        except:
            return api_response(400, "account delete failed. no account found of this user", {}, status=False)
