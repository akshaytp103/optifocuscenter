from django.urls import path
from django.urls import path
from . import views

urlpatterns = [
    # path('register/',views.register,name='register'),
    path('login/', views.login, name='login'),
    path('verify-otp/', views.verify_otp, name='verify_otp'),
    path('doctors_table/', views.doctors_table, name='doctors_table'),
    path('patients_table/', views.patients_table, name='patients_table'),
    path('patientlist_for_each_dr/<str:id>/', views.patientlist_for_each_dr, name='patientlist_for_each_dr'),
  
    
    
]


