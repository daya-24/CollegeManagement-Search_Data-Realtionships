from django.db import models
from DepartmentApp.models import Department
# Create your models here.
class Faculty(models.Model):
    department = models.ManyToManyField(Department, related_name='department_fac')
    Faculty_ID = models.IntegerField()
    Faculty_Name = models.CharField(max_length=32)
    Faculty_Salary = models.FloatField()

    def __str__(self):
        return f"{self.department}, {self.Faculty_ID},{self.Faculty_Name},{self.Faculty_Salary}"