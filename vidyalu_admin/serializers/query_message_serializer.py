from rest_framework import serializers

from vidyalu_admin.models.query_message_model import QueryMessageModel

class QueryMessageSerializer(serializers.ModelSerializer):
    class Meta:
            model = QueryMessageModel
            fields = '__all__'
