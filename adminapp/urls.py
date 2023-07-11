
from django.urls import path
from . import views


urlpatterns = [
    path('admin_home',views.admin_home,name='admin_home'),
    path('admin_login',views.admin_login,name='admin_login'),
    path('doctors_list/',views.doctors_list,name='doctors_list'),
    path('patients_list/',views.patients_list,name='patients_list'),
    path('Patients_edit/<str:id>/', views.Patients_edit,name='Patients_edit'),
    path('doctors_edit/<str:id>/', views.doctors_edit,name='doctors_edit'),
    path('add_doctor/', views.add_doctor,name='add_doctor'),
    path('admin_logout/', views.admin_logout,name='admin_logout'),
    path('doctor_delete/<str:id>/', views.doctor_delete,name='doctor_delete'),
  
]