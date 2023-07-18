from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.utils.crypto import get_random_string
from accounts.models import *
from .models import OTP
import random
from django.conf import settings
from django.contrib import messages, auth
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.core.mail import EmailMessage






def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        token = str(random.randint(100000, 999999))
        OTP.objects.update_or_create(email=email, defaults={'token': token})
        send_mail(
            'OTP for Login',
            f'Your OTP is : {token}',     
            'lothbrok007007@gmail.com',
            [email],
            fail_silently=False,
        )
        return render(request, 'otplogin/verify_otp.html', {'email': email})
    return render(request, 'otplogin/send_otp.html')


def verify_otp(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        otp = request.POST.get('otp')
        otp_obj = OTP.objects.filter(email=email, token=otp).order_by('-created_at').first()
        if otp_obj:
            # OTP is valid
            otp_obj.delete()  # Remove the OTP from the database after verification
            # Add your logic here to log in the user or redirect to the appropriate page
            return redirect('doctors_table')
        else:
            # OTP is invalid
            messages.error(request, "Incorrect OTP") 
    return redirect('login')

def doctors_table(request):
    admin_dr=Doctor.objects.all()
    context={
        'admin_dr': admin_dr,
    }
    return render(request, "otplogin/doctorlist.html",context)

def patients_table(request):
    patlist=account.objects.all()   
    context={
        'patlist' : patlist,
       
    }
    return render(request, "otplogin/patient_table.html",context)



# def patientlist_for_each_dr(request,id):
#     related_id = id
#     doct_values = account.objects.filter(selectdoctor__id=related_id).values_list('selectdoctor__name', flat=True).distinct()
    
#     distinct_values = account.objects.values_list('selectdoctor', flat=True).distinct()
#     print(222,distinct_values)

#     # Step 3: Iterate over each distinct value and filter the model
#     for value in distinct_values:
#         condition = Q(selectdoctor=value)  
#         print(444,condition)     
#         # Apply the filter to the model and retrieve the results
#         results = account.objects.filter(condition)
#         print(111,id,results)
#         context={
#             'results': results,
#             'doct_values' :doct_values
#         }
#         return render (request, 'otplogin/patientlistfordr.html',context)

def patientlist_for_each_dr(request,id):
    related_id = id
    doct_values = account.objects.filter(selectdoctor__id=related_id).values_list('selectdoctor__name', flat=True).distinct()
    
    results = account.objects.filter(selectdoctor__id=related_id)
    context={
        'results': results,
        'doct_values' :doct_values
    } 
    return render (request, 'otplogin/patientlistfordr.html',context)



