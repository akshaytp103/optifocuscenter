
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('about',views.about,name='about'),
    path('appointment',views.appointment,name='appointment'),
    path('contact',views.contact,name='contact'),
    path('department',views.department,name='department'),
    path('search',views.search,name='search'),
    path('view_appointment/',views.view_appointment,name='view_appointment'),
    path('appointments_pdf/<str:id>/',views.appointments_pdf,name='appointments_pdf'),
    path('pdf_report_create/', views.pdf_report_create, name='pdf_report_create'),
    
    
    
] 