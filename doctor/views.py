from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.conf import settings
from django.utils.crypto import get_random_string
from accounts.models import account
from .forms import EmailForm
# from .models import OTP

# def send_otp(request):
#     if request.method == 'POST':
#         form = EmailForm(request.POST)
#         if form.is_valid():
#             email = form.cleaned_data['email']
#             user, created = account.objects.get_or_create(email=email)

#             # Generate a 6-digit OTP
#             otp = get_random_string(length=4, allowed_chars='0123456789')

#             # Store the OTP in the database
#             otp_obj = OTP(user=user, otp_code=otp)
#             otp_obj.save()

#             # Send the OTP to the user's email address
#             subject = 'OTP Verification'
#             message = f'Your OTP is: {otp}'
#             from_email = settings.DEFAULT_FROM_EMAIL
#             to_email = [email]
#             send_mail(subject, message, from_email, to_email)

#             return redirect('verify_otp')
#     else:
#         form = EmailForm()
    
#     return render(request, 'send_otp.html', {'form': form})

# def verify_otp(request):
#     if request.method == 'POST':
#         otp = request.POST.get('otp')
#         user = request.user

#         # Check if the OTP matches the one stored in the database
#         otp_obj = OTP.objects.filter(user=user, otp_code=otp).first()
#         if otp_obj:
#             # OTP is valid
#             otp_obj.delete()  # Remove the OTP from the database
#             return redirect('home')
#         else:
#             # OTP is invalid
#             return redirect('verify_otp')

#     return render(request, 'verify_otp.html')
