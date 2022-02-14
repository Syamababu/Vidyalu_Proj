from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from core.permissions import IsAdmin
from core.helpers import api_response

from vidyalu_admin.models.course_session_category_models import CourseSesssionCategoryModel

from vidyalu_admin.serializers.course_session_category_serializer import CourseSessionCategorySerializer

class CourseSessionCategoryView(APIView):

    permission_classes = (IsAdmin,)

    def post(Self, request):

        serializer = CourseSessionCategorySerializer(data = request.data)

        if serializer.is_valid():
            serializer.save()
            return api_response(200, 'category saved successfully', serializer.data, status=True)

        return api_response(400, 'category save failed', {}, status=False)

    def put(self, request):
        try:
            category = CourseSesssionCategoryModel.objects.get(id = request.data['id'])
            serializer = CourseSessionCategorySerializer(data = request.data,instance=category, partial = True)
            if serializer.is_valid():
                serializer.save()
                return api_response(200, "category updated succesfully", serializer.data, status=True)
        except:
            return api_response(400, "category update failed", {}, status=False)
            
    def delete(self, request):
        try:
            category = CourseSesssionCategoryModel.objects.get(id = request.data['id'])
            category.delete()
            return api_response(200, "category deleted", {}, status=True)
        except:
            return api_response(400, "course delete failed", {}, status=False)

class GetCourseSessionCategoryView(APIView):
    
    permission_classes = (IsAdmin,)

    def post(self, request):
        try:
            category_type = request.data['category_type']
            serializer = CourseSessionCategorySerializer(CourseSesssionCategoryModel.objects.filter(category_type = category_type), many = True)
            return api_response(200, 'category fetched successfully', serializer.data, status=True)
        except:
            serializer = CourseSessionCategorySerializer(CourseSesssionCategoryModel.objects.all(), many = True)
            return api_response(200, 'category fetched successfully', serializer.data, status=True)


class DeleteCourseSessionCategoryView(APIView):
    permission_classes = (IsAdmin,)

    def post(self, request):
        try:
            category = CourseSesssionCategoryModel.objects.get(id = request.data['id'])
            category.delete()
            return api_response(200, "category deleted", {}, status=True)
        except:
            return api_response(400, "course delete failed", {}, status=False)