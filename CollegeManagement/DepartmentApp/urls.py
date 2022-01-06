from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.AddDepartmentView.as_view(), name='add_dept'),
    path('show/', views.ShowDepartmentView.as_view(), name='show_dept'),
    path('delete/<int:i>', views.DeleteDepartmentView.as_view(), name='delete_dept'),
    path('update/<int:i>', views.UpdateDepartmentView.as_view(), name='update_dept'),

]