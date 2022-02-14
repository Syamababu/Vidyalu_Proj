from rest_framework import serializers
from student.models.student_test_model import StudentTest
from teacher.models.teacher_test_model import Test
from student.models.student_test_result import TestResult

class StudentAnswerGetSerializer(serializers.ModelSerializer):

    class Meta:
        model = StudentTest
        fields = "__all__"


class StudentResultGetSerializer(serializers.ModelSerializer):

    class Meta:
        model = TestResult
        fields = ["id","student","test","created_at","updated_at"]

class StudentGetSerializer(serializers.ModelSerializer):

    class Meta:
        model = StudentTest
        fields = ["test_attempt",]



class StudentTestGetSerializer(serializers.ModelSerializer):
    attempt = serializers.SerializerMethodField(default=False)

    class Meta:
        model = Test
        fields = "__all__"


    def get_attempt(self, obj):
        try:
            user_id = self.context['user_id']
            test_id = obj.id
            # print(test_id)
            stu = StudentTest.objects.get(test_id=test_id,student_id=user_id)
            # serializer1 = StudentGetSerializer(stu)
            # data1 = serializer1.data
            # return data1
            return stu.test_attempt
        except StudentTest.DoesNotExist:
            return None


# class StudentTestPostSerializer(serializers.ModelSerializer):
#     # start_date = serializers.DateField(required=False)
#     # duration = serializers.DurationField(required=False)
#     class Meta:
#         model = StudentTest
#         exclude = ["student"]
#         # fields = ('title','course','no_of_question','start_date','duration','end_date','total_marks')
#
