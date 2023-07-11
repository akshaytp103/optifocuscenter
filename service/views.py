from django.shortcuts import render
from .models import *

# Create your views here.

def cataract(request):
    result = Service.objects.filter(name__icontains='cataract')
    # result = Service.objects.all()
    return render(request, 'service/cataract.html',{'result':result})

def corneal(request):
    co_res= Service.objects.filter(name__icontains='corneal')
    return render(request, 'service/corneal.html',{'co_res':co_res}) 

def Glaucoma(request):
    gl_res= Service.objects.filter(name__icontains='Glaucoma')
    return render(request, 'service/glaucoma.html',{'gl_res':gl_res})

def diabetic_retinopathy(request):
    de_res = Service.objects.filter(name__icontains='diabeticretinopathy')
    return render(request, 'service/deabetic.html',{'de_res':de_res})