from rest_framework import serializers
from student.models.student_session_test import StudentSessionTest
from counsellor.models.counsellor_test_model import CounsellorTest
from student.models.student_sessiontest_result import SessionTestResult

class StudentAnswerSerializer(serializers.ModelSerializer):

    class Meta:
        model = StudentSessionTest
        fields = "__all__"


class StudentSessionResultGetSerializer(serializers.ModelSerializer):

    class Meta:
        model = SessionTestResult
        # fields = ["id","student","test","created_at","updated_at"]
        fields = "__all__"

# class StudentGetSerializer(serializers.ModelSerializer):
#
#     class Meta:
#         model = StudentTest
#         fields = ["test_attempt",]
#


class StudentSessionTestSerializer(serializers.ModelSerializer):
    attempt = serializers.SerializerMethodField(default=False)

    class Meta:
        model = CounsellorTest
        fields = "__all__"


    def get_attempt(self, obj):
        try:
            user_id = self.context['user_id']
            test_id = obj.id
            # print(test_id)
            stu = StudentSessionTest.objects.get(test_id=test_id,student_id=user_id)
            # serializer1 = StudentGetSerializer(stu)
            # data1 = serializer1.data
            # return data1
            return stu.test_attempt
        except StudentSessionTest.DoesNotExist:
            return None


# class StudentTestPostSerializer(serializers.ModelSerializer):
#     # start_date = serializers.DateField(required=False)
#     # duration = serializers.DurationField(required=False)
#     class Meta:
#         model = StudentTest
#         exclude = ["student"]
#         # fields = ('title','course','no_of_question','start_date','duration','end_date','total_marks')
#
