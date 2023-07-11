from django.shortcuts import render,redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages, auth
from accounts.models import Doctor,account
from accounts.forms import *




# Create your views here.
def admin_home(request):  
    patcount=account.objects.count()
    doccount=Doctor.objects.count()
    context={
        'patcount':patcount,
        'doccount':doccount
    }
    return render (request,'admin/admindash.html',context)

def admin_login(request):
    if request.user.is_authenticated:
        return redirect("admin_home")

    if request.method == "POST":
        name = request.POST["name"]
        password = request.POST["password"]
        user = auth.authenticate(username=name, password=password,is_superadmin=True)

        if user is not None:
            auth.login(request, user)
            messages.success(request, "Login Successful")
            return redirect("admin_home") 
        else: 
            messages.error(request, "you are not an admin")
            return redirect("admin_login")

    else:
        return render(request, "admin/login.html")
    

def doctors_list(request):
    drlist=Doctor.objects.all()
    context={
        'drlist': drlist,
    }
    return render(request, "admin/doctors.html",context)

def patients_list(request):
    patlist=account.objects.all()   
    context={
        'patlist' : patlist,
       
    }
    return render(request, "admin/patients.html",context)
    
def Patients_edit(request, id) :
    Patients = account.objects.get(id=id)
    if request.method == 'POST' :
        form = Patientform(request.POST, request.FILES, instance=Patients)   
        if form.is_valid() :
            form.save() 
            return redirect('patients_list') 
        
    form = Patientform(instance=Patients) 
    context = {'form' : form} 
    return render(request, 'admin/addpatients.html', context) 

def doctors_edit(request, id) :
    doctor = Doctor.objects.get(id=id)
    if request.method == 'POST' :
        form = Doctorform(request.POST, request.FILES, instance=doctor)   
        if form.is_valid() :
            form.save() 
            return redirect('doctors_list') 
        
    form = Doctorform(instance=doctor) 
    context = {'form' : form} 
    return render(request, 'admin/editdoctors.html', context) 


def add_doctor(request):
    if request.method == "POST":
        form = Doctorform(request.POST,request.FILES)
        if form.is_valid():          
            form.save()
            return redirect('doctors_list') 
        else:
            print('not added')
            messages.info(request,'not added')
    else:
        form = Doctorform()
    return render(request,'admin/adddoctor.html',{'form':form})


def admin_logout(request):
    auth.logout(request)
    return redirect("admin_login")

def doctor_delete(request, id) : 
    doct = Doctor.objects.get(id=id)
    context = {'doct' : doct}
    
    if request.method == 'POST' :
        doct.delete()
        return redirect('doctors_list') 
    
    return render(request, 'admin/doctdelete.html', context) 



