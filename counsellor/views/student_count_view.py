
from rest_framework.views import APIView
from core.permissions import IsCounsellor
from core.helpers import api_response
from student.models.session_booking import SessionBooking
#from teacher.serializers.student_list_serializer import CoursebookingStudentSerializer
#from student.serializers.student_serializer import StudentSerializer
#from student.models.students import Student
from counsellor.models.session_model import Session



class CounsellorCountStudentView(APIView):
    permission_classes = (IsCounsellor,)

    def get(self,request):
        counsellor_id = request.user.id
        if counsellor_id:
            student_list = SessionBooking.objects.filter(counsellor_id=counsellor_id,is_booking=True)
            stu_list = [stu.user.id for stu in student_list]
            stu_count = len(stu_list)
            sum = 0
            for session in student_list:
                print(session.session_id)
                session = Session.objects.filter(id=session.session_id)
                for obj in session:
                    sum += obj.price
            print(sum)
            # stu_cont = [stu.user.id for stu in student_list]
            return api_response(200, "Student count retrieved successfully", [{"stu_count": stu_count,"my_earning":sum}],status=True)
        else:
            return api_response(200, "No student found", [], status=True)
