from rest_framework.views import APIView

from vidyalu_admin.serializers.news_letter_email_serializer import NewsLetterEmailSerializer
from vidyalu_admin.models.news_letter_email_model import NewsLetterEmailModel

from core.helpers import api_response
from core.permissions import IsAdmin

class PostNewsLetterEmailView(APIView):

    def post(self, request):
        serializer = NewsLetterEmailSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return api_response(200, "News later saved success fully", {}, status=True)

        return api_response(400, "News later save failed", {}, status=False)

class GetNewsLetterEmailView(APIView):
    
    permission_classes = (IsAdmin,)

    def get(self, request):
        try:
            news_latters = reversed(NewsLetterEmailModel.objects.all())#.reverse()
            serializer = NewsLetterEmailSerializer(instance=news_latters, many = True)
            return api_response(200, "news letters fetched successfully", serializer.data, status=True)
        except:
            return api_response(400, "News letter fetch failed", {}, status=False)