from django.db import models
from DepartmentApp.models import Department
# Create your models here.
class Student(models.Model):
    department = models.ForeignKey(Department, related_name='department_stud', on_delete=models.CASCADE)
    Roll_No = models.IntegerField()
    Student_Name = models.CharField(max_length=32)
    Grade = models.CharField(max_length=32)


    def __str__(self):
        return f"{self.department}, {self.Roll_No},{self.Student_Name},{self.Grade}"