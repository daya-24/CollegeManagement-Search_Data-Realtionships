from django.contrib import admin
from .models import Faculty
# Register your models here.

class FacultyAdmin(admin.ModelAdmin):
   list_display = ['Faculty_ID', 'Faculty_Name', 'Faculty_Salary']

admin.site.register(Faculty,FacultyAdmin)