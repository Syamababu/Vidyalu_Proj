from django.db import models
from core.models.users import User
from teacher.models.courses_model import Course


class CourseRating(models.Model):
    """
            Student Course Rating model.
    """
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name='student_courserateing_user',null=True)
    teacher = models.ForeignKey(User, on_delete=models.CASCADE,related_name='teacher_rating_user',null=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE,null=True)
    review = models.CharField(max_length=5000,null=True,blank=True)
    rating = models.IntegerField(null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    class Meta:
        db_table = "course_rating"
        verbose_name = "Course_rating"
        verbose_name_plural = "Course_rating"


