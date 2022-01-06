from django.shortcuts import render, redirect
from .forms import FacultyForm
from .models import Faculty
from django.views import View
# Create your views here.

class AddFacultyView( View):
    def get(self, request):
        form = FacultyForm()

        context = {'form': form}
        templates_name = 'FacultyApp/add_fac.html'
        return render(request, templates_name, context)

    def post(self, request):

        form = FacultyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show_fac')
        context = {'form': form}
        templates_name = 'FacultyApp/add_fac.html'
        return render(request, templates_name, context)



class ShowFacultyView(View):
    def get(self, request):
        show_obj = Faculty.objects.all()
        templates_name = 'FacultyApp/show_fac.html'
        context = {'show_obj': show_obj}
        return render(request, templates_name, context)

    def post(self, request):
        show_obj = Faculty.objects.filter(Faculty_Name__icontains=request.POST['searchdata'])

        template_name = 'FacultyApp/show_fac.html'
        context = {'show_obj': show_obj}
        return render(request, template_name, context)

class DeleteFacultyView( View):
    def get(self, request, i):
        var1 = Faculty.objects.get(id=i)
        var1.delete()
        return redirect('show_fac')


class UpdateFacultyView( View):
    def get(self, request, i):
        s2 = Faculty.objects.get(id=i)
        form = FacultyForm(instance=s2)

        context = {'form': form}
        templates_name = 'FacultyApp/add_fac.html'
        return render(request, templates_name, context)

    def post(self, request, i):
        s2 = Faculty.objects.get(id=i)
        form = FacultyForm(request.POST, instance=s2)
        if form.is_valid():
            form.save()
            return redirect('show_fac')