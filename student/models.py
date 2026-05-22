from django.db import models
from course.models import Course
# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length = 100)
    parent_name = models.CharField(max_length = 100)
    phone_number = models.CharField()
    email = models.EmailField()
    age = models.IntegerField()
    course=models.ForeignKey(Course,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name

