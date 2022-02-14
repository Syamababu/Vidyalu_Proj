from rest_framework import serializers
from vidyalu_admin.models.support_number_email import SupportNumberEmail

class SupportNumberEmailSerializer(serializers.ModelSerializer):
    class Meta:
        model = SupportNumberEmail
        fields = '__all__'