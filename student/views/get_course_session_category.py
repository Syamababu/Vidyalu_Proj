from rest_framework.views import APIView

from core.permissions import IsStudentTeacherCounsellor

from core.helpers import api_response

from vidyalu_admin.models.course_session_category_models import CourseSesssionCategoryModel
from vidyalu_admin.serializers.course_session_category_serializer import CourseSessionCategorySerializerViewOnly

class CourseSessionCategoryViewOnly(APIView):
    permission_classes = (IsStudentTeacherCounsellor,)

    def get(self, request):
        try:
            course_category = reversed(CourseSesssionCategoryModel.objects.filter(category_type = 'course', is_active = True))
            serializer1 = CourseSessionCategorySerializerViewOnly(instance=course_category, many = True)
            session_category = reversed(CourseSesssionCategoryModel.objects.filter(category_type = 'session', is_active = True))
            serializer2 = CourseSessionCategorySerializerViewOnly(instance=session_category, many = True)
            return api_response(200, "course session category fetched", [{'course_category':serializer1.data, 'session_category':serializer2.data}], status= True)
        except:
            return api_response(400, "course session category retrive failed", {}, status=False)

