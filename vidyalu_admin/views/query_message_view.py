from rest_framework.views import APIView

from vidyalu_admin.models.query_message_model import QueryMessageModel

from vidyalu_admin.serializers.query_message_serializer import QueryMessageSerializer

from core.helpers import api_response
from core.permissions import IsAdmin

class QueryMessageView(APIView):
    # def get(self, request):
    #     pass
    def post(self, request):
        serializer = QueryMessageSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return api_response(200, "Message send successfully", {}, status=True)
        return api_response(400, "Message send failed",{}, status=False)

class QueryMessageAdminView(APIView):
    permission_classes = (IsAdmin,)
    def get(self, request):
        try:
            query_message = QueryMessageModel.objects.all()
            serializer = QueryMessageSerializer(query_message, many = True)
            return api_response(200, "Query  messages fetched successfully", serializer.data, status=True)
        except:
            return api_response(400, "Unable to fetch query message", {}, status=False)
