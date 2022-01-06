from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.AddStudentView.as_view(), name='add_stud'),
    path('show/', views.ShowStudentView.as_view(), name='show_stud'),
    path('delete/<int:i>', views.DeleteStudentView.as_view(), name='delete_stud'),
    path('update/<int:i>', views.UpdateStudentView.as_view(), name='update_stud'),

]