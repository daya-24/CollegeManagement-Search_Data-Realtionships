import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'CollegeManagement.settings')
import django
django.setup()

from DepartmentApp.models import *
from FacultyApp.models import *
from StudentApp.models import *

from faker import Faker
from random import *

fake = Faker()


def populate(n):
    for i in range(n):
        fname = fake.Department_Name()
        fsub = fake.subject()

        department_record = Department.objects.get_or_create(Department_name=fname, subject=fsub)

populate(200)