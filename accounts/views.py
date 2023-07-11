
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect,HttpResponse
from django.contrib import messages, auth
from .forms import Patientform



from .models import *

# from .forms import AppointmentForm

# Create your views here.
def home(request):
    return render(request, 'index.html')

def about(request): 
    return render(request, 'about.html')


def appointment(request):
    if request.method == "POST":
        form = Patientform(request.POST,request.FILES)
        if form.is_valid():          
            form.save()
            print(11111)
            return redirect('home') 
        else:
            print('not added')
            messages.info(request,'not added')
    else:
        form = Patientform()
    return render(request,'appointment.html',{'form':form})

def contact(request):
    return render(request, 'contact.html')

def department(request):
    return render(request, 'department.html')



def search(request):
    search_doct =Doctor.objects.all()
    return render(request, 'search.html', {'search_doct': search_doct})
    
def view_appointment(request):
    appoi=account.objects.all()
    return render(request, 'view_appointment.html',{'appoi':appoi})