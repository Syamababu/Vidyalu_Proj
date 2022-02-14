from core import serializers
from core.helpers import api_response
from rest_framework.views import APIView
from core.models.users import User
from student.models.students import Student
from teacher.models.teachers import Teacher
from counsellor.models.counsellors import Counsellor
from core.helpers import api_response
from rest_framework.permissions import IsAuthenticated
from student.serializers.student_serializer import StudentSerializer
from teacher.serializers.teacher_serializer import TeacherSerializer
from counsellor.serializers.counsellor_serializer import CounsellorSerializer
from django.db.models import Q
from teacher.models.courses_model import Course
from counsellor.models.session_model import Session

class SearchView(APIView):
    """
       Student can able to search teacher or counsellor.
     """
    def post(self, request):
        self.role = request.data.get("role", None)
        self.city = request.data.get("city", None)
        self.state = request.data.get("state", None)
        self.search = request.data.get("search", None)
        self.category = request.data.get("category",None)

        if self.role == "teacher":
            data = self.teacher_search()
            if data:
                return api_response(200, "Teacher search results", data, status=True)
            else:
                return api_response(200, "No result found", [], status=True)

        if self.role == "counsellor":
            data = self.counsellor_search()
            if data:
                return api_response(200, "Counsellor search results", data, status=True)
            else:
                return api_response(200, "No result found", [], status=True)
        return api_response(200, "search results", [], status=False)

    def teacher_search(self):
        # tch_objs = Teacher.objects.filter(step=3)
        if self.category:
            print(self.category)
            tids = Course.objects.filter(teacher_category=self.category).values_list("teacher_id", flat=True).distinct()
            tch_objs = Teacher.objects.filter(teacher_id__in=tids,step=3)

            if self.city:
                tch_objs = tch_objs.filter(teacher__city=self.city,step=3)

            if self.state:
                tch_objs = tch_objs.filter(teacher__state=self.state,step=3)

            if self.search:
                tch_objs = tch_objs.filter(Q(teacher__area_code__icontains=self.search,step=3) | Q(search__icontains=self.search,step=3))

            serializer = TeacherSerializer(tch_objs, many=True)
            return serializer.data
        else:
            tch_objs = Teacher.objects.filter(step=3)
            if self.city:
                # print("except",self.city)
                tch_objs = tch_objs.filter(teacher__city=self.city)

            if self.state:
                tch_objs = tch_objs.filter(teacher__state=self.state)

            if self.search:
                tch_objs = tch_objs.filter(
                    Q(teacher__area_code__icontains=self.search) | Q(search__icontains=self.search))
                # tch_objs =tch_objs.filter(search__icontains=self.search)
            serializer = TeacherSerializer(tch_objs, many=True)
            return serializer.data



    def counsellor_search(self):
        if self.category:
            print(self.category)
            cids = Session.objects.filter(counsellor_category=self.category).values_list("counsellor_id", flat=True).distinct()
            cons_objs = Counsellor.objects.filter(counsellor_id__in=cids, step=3)

            if self.city:
                cons_objs = cons_objs.filter(counsellor__city=self.city,step=3)

            if self.state:
                cons_objs = cons_objs.filter(counsellor__state=self.state,step=3)

            if self.search:
                cons_objs = cons_objs.filter(Q(counsellor__area_code__icontains=self.search,step=3) | Q(search__icontains=self.search,step=3))
                # cons_objs = cons_objs.filter(search__icontains=self.search)

            serializer = CounsellorSerializer(cons_objs, many=True)
            return serializer.data
        else:
            cons_objs = Counsellor.objects.filter(step=3)
            if self.city:
                cons_objs = cons_objs.filter(counsellor__city=self.city)

            if self.state:
                cons_objs = cons_objs.filter(counsellor__state=self.state)

            if self.search:
                cons_objs = cons_objs.filter(
                    Q(counsellor__area_code__icontains=self.search) | Q(search__icontains=self.search))
                # cons_objs = cons_objs.filter(search__icontains=self.search)

            serializer = CounsellorSerializer(cons_objs, many=True)
            return serializer.data






