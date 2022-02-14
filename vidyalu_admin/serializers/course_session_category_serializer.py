from rest_framework import serializers

from vidyalu_admin.models.course_session_category_models import CourseSesssionCategoryModel

class CourseSessionCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseSesssionCategoryModel
        fields = ('id', 'category_type', 'category', 'is_active')

class CourseSessionCategorySerializerViewOnly(serializers.ModelSerializer):
    class Meta:
        model = CourseSesssionCategoryModel
        fields = ("id", "category")