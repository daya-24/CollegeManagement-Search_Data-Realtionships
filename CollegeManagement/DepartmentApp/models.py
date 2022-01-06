from django.db import models

# Create your models here.
class Department(models.Model):
    Department_Name = models.CharField(max_length=32)
    Intake = models.IntegerField()

    def __str__(self):
        return f"{self.Department_Name}, {self.Intake}"