from rest_framework import serializers

from vidyalu_admin.models.competecy_areas_model import CompetencyAreasModel

class CompetencyAreasSerializer(serializers.ModelSerializer):

    class Meta:
        model = CompetencyAreasModel
        fields = '__all__'

class CompetencyAreasViewOnlySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = CompetencyAreasModel
        fields = ('id','competency_area')