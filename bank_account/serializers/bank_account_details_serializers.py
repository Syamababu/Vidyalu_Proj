from rest_framework import serializers

from bank_account.models.account_details import AccountDetails

from core.models.users import User

from core.serializers.auth_serializer import UserSerializer

class BankAccountSerializer(serializers.ModelSerializer):
    # user = serializers.SerializerMethodField()
    class Meta:
        model = AccountDetails
        fields = '__all__'

    # def get_user(self, obj):
    #     try:
    #         user_id = obj.id
    #         user = User.objects.get(id=user_id)
    #         serializer = UserSerializer(user)
    #         return serializer.data
    #     except User.DoesNotExist:
    #         return None
