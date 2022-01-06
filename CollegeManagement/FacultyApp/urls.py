from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.AddFacultyView.as_view(), name='add_fac'),
    path('show/', views.ShowFacultyView.as_view(), name='show_fac'),
    path('delete/<int:i>', views.DeleteFacultyView.as_view(), name='delete_fac'),
    path('update/<int:i>', views.UpdateFacultyView.as_view(), name='update_fac'),

]