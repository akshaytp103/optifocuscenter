from django import forms    
from . models import *


# class AppointmentForm(forms.ModelForm):
#     selectdoctor = forms.ModelChoiceField(queryset=doctor.objects.all())
    
#     class Meta:
#         model=account
#         fields=['name','email','phone','appointmentdate','appointmenttime','selectdoctor','message']
#         # fields = '__all__'
        

#     def __init__(self,*args,**kwargs):
#         super(AppointmentForm ,self).__init__(*args,**kwargs)

#         for field in self.fields:
#             self.fields[field].widget.attrs['class']='form-control'

#     def clean(self):
#         cleaned_data    =super(AppointmentForm,self).clean()


class Patientform(forms.ModelForm):
    class Meta:
        model = account
        fields = ("name", "password", "email", "phone", "appointmentdate", 
                  "appointmenttime","selectdoctor","message")
        
    def __init__(self, *args, **kwargs):
        super(Patientform, self).__init__(*args, **kwargs)
        
        for field in self.fields:
            self.fields[field].widget.attrs["class"] = "form-control"
            
class Doctorform(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = ["name","availabledate", "email", "availabetime","profile_pic","mobile","department","status"]
        
    def __init__(self, *args, **kwargs):
        super(Doctorform, self).__init__(*args, **kwargs)
        
        for field in self.fields:
            self.fields[field].widget.attrs["class"] = "form-control"