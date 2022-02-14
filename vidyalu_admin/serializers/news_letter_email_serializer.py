from rest_framework import serializers

from vidyalu_admin.models.news_letter_email_model import NewsLetterEmailModel

class NewsLetterEmailSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsLetterEmailModel
        fields = '__all__'