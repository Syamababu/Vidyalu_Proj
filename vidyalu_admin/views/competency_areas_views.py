from rest_framework.views import APIView

from core.permissions import IsAdmin, IsStudentTeacherCounsellor
from core.helpers import api_response

from vidyalu_admin.models.competecy_areas_model import CompetencyAreasModel
from vidyalu_admin.serializers.compentency_areas_seralizer import CompetencyAreasSerializer, CompetencyAreasViewOnlySerializer

class CompetencyAreasView(APIView):
    permission_classes = (IsAdmin,)

    def get(self, request):
        competency_areas = reversed(CompetencyAreasModel.objects.all())
        serializer = CompetencyAreasSerializer(instance=competency_areas, many = True)
        return api_response(200, "competency areas fetched successfully", serializer.data, status=True)

    def post(self, request):
        print("Hello")
        try:
            serializer = CompetencyAreasSerializer(data = request.data)
            print(request.data)
            print(serializer.initial_data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return api_response(200, "competence saved succesfully", [serializer.data], status=True)
            return api_response(400,"competency save failed", {}, status=False)
        except:
            return api_response(400,"competency save failed", {}, status=False)

    def put(self, request):
        try:
            competency = CompetencyAreasModel.objects.get(id = request.data['id'])
            serializer = CompetencyAreasSerializer(instance=competency, data= request.data, partial = True)
            if serializer.is_valid():
                serializer.save()
                return api_response(200, "competency updated succesfully", [serializer.data], status=True)
            return api_response(400, "competency update failed", {}, status=True)
        except:
            return api_response(400, "competency update failed", {}, status=True)

class CompetencyAreasViewOnly(APIView):
    
    permission_classes = (IsStudentTeacherCounsellor,)

    def get(self, request):
        try:
            competency = reversed(CompetencyAreasModel.objects.filter(is_active = True))
            serializer = CompetencyAreasViewOnlySerializer(instance=competency, many = True)
            return api_response(200, "competency fetched succesfully", serializer.data, status=True)
        except:
            return api_response(400, "competency fetch failed", {}, status=False)

class DeleteCompetencyArea(APIView):
    permission_classes = (IsAdmin,)

    def post(self, request):
        try:
            competency = CompetencyAreasModel.objects.get(id = request.data['id'])
            competency.delete()
            return api_response(200, "competency deleted succesfully", {}, status = True)
        except:
            return api_response(400, "competency delete failed", {}, status=False)