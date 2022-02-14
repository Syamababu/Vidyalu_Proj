from rest_framework import serializers

from counsellor.models.counsellor_question_model import CounsellorQuestion

class CounsellorQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = CounsellorQuestion
        exclude = ["counsellor"]



class CounsellorQuestionGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = CounsellorQuestion
        fields = '__all__'





# class TeacherQuestionFilePostSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Question
#         fields = ('question_text','option_one','option_two','option_three','option_four','correct_answer')
#
