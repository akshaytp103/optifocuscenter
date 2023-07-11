from django.db import models
from django.contrib.auth.models import User




# Create your models here.
class Doctor(models.Model):  
    name = models.CharField(max_length=20)
    email = models.EmailField(max_length=50,null=True)
    availabledate=models.DateField(auto_now_add=False) 
    availabetime = models.TimeField(auto_now=False)
    profile_pic= models.ImageField(upload_to='media',null=True,blank=True)
    mobile = models.CharField(max_length=20,null=True)
    department= models.CharField(max_length=50)
    status=models.BooleanField(default=False)
    
    def __str__(self):      
        return self.name

    
class account(models.Model):
      
    name = models.CharField( max_length = 50, blank = False,null = False)
    password=models.CharField(max_length=100,null=True)
    email = models.EmailField(blank = False, null = False)
    phone = models.CharField(max_length = 10,)
    appointmentdate = models.CharField(max_length = 10,)
    appointmenttime = models.CharField(max_length = 10,)
    selectdoctor = models.ForeignKey(Doctor, on_delete=models.CASCADE) 
    message = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name 
    
    



    
    
    
    