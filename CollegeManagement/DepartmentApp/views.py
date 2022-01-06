from django.shortcuts import render, redirect
from .forms import DepartmentForm
from .models import Department
from django.views import View
# Create your views here.

class AddDepartmentView( View):
    def get(self, request):
        form = DepartmentForm()

        context = {'form': form}
        templates_name = 'DepartmentApp/add_dept.html'
        return render(request, templates_name, context)

    def post(self, request):

        form = DepartmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show_dept')
        context = {'form': form}
        templates_name = 'DepartmentApp/add_dept.html'
        return render(request, templates_name, context)



class ShowDepartmentView(View):
    def get(self, request):
        show_obj = Department.objects.all()
        templates_name = 'DepartmentApp/show_dept.html'
        context = {'show_obj': show_obj}
        return render(request, templates_name, context)

    def post(self, request):
        department = Department.objects.filter(Department_Name__icontains=request.POST['searchdata'])
        faculty = department[0].department_fac.all()
        student = department[0].department_stud.all()

        template_name = "DepartmentApp/searchinfo.html"
        context = {'department': department, 'faculty': faculty, 'student': student}
        return render(request, template_name, context)


class DeleteDepartmentView( View):
    def get(self, request, i):
        var1 = Department.objects.get(id=i)
        var1.delete()
        return redirect('show_dept')


class UpdateDepartmentView( View):
    def get(self, request, i):
        s2 = Department.objects.get(id=i)
        form = DepartmentForm(instance=s2)

        context = {'form': form}
        templates_name = 'DepartmentApp/add_dept.html'
        return render(request, templates_name, context)

    def post(self, request, i):
        s2 = Department.objects.get(id=i)
        form = DepartmentForm(request.POST, instance=s2)
        if form.is_valid():
            form.save()
            return redirect('show_dept')

