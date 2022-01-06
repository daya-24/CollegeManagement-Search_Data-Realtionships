from django.contrib import admin
from .models import Student
# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    list_display = ['Roll_No', 'Student_Name', 'Grade']

admin.site.register(Student,StudentAdmin)