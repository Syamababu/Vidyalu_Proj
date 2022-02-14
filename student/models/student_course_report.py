from django.db import models
from core.models.users import User
from teacher.models.courses_model import Course


class CourseReport(models.Model):
    """
            Student Course Report model.
    """
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name='student_coursereport_user',null=True)
    teacher = models.ForeignKey(User, on_delete=models.CASCADE,related_name='teacher_report_user',null=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE,null=True)
    report = models.CharField(max_length=5000,null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    class Meta:
        db_table = "course_report"
        verbose_name = "Course_report"
        verbose_name_plural = "Course_report"


