from django.shortcuts import render, redirect
from .forms import StudentForm
from .models import Student
from django.views import View
# Create your views here.

class AddStudentView( View):
    def get(self, request):
        form = StudentForm()

        context = {'form': form}
        templates_name = 'StudentApp/add_stud.html'
        return render(request, templates_name, context)

    def post(self, request):

        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show_stud')
        context = {'form': form}
        templates_name = 'StudentApp/add_stud.html'
        return render(request, templates_name, context)



class ShowStudentView(View):
    def get(self, request):
        show_obj = Student.objects.all()
        templates_name = 'StudentApp/show_stud.html'
        context = {'show_obj': show_obj}
        return render(request, templates_name, context)

    def post(self, request):
        show_obj = Student.objects.filter(Student_Name__icontains=request.POST['searchdata'])

        template_name = 'StudentApp/show_stud.html'
        context = {'show_obj': show_obj}
        return render(request, template_name, context)

class DeleteStudentView( View):
    def get(self, request, i):
        var1 = Student.objects.get(id=i)
        var1.delete()
        return redirect('show_stud')


class UpdateStudentView( View):
    def get(self, request, i):
        s2 = Student.objects.get(id=i)
        form = StudentForm(instance=s2)

        context = {'form': form}
        templates_name = 'StudentApp/add_stud.html'
        return render(request, templates_name, context)

    def post(self, request, i):
        s2 = Student.objects.get(id=i)
        form = StudentForm(request.POST, instance=s2)
        if form.is_valid():
            form.save()
            return redirect('show_stud')