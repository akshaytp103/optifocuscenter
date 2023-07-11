from django.urls import path
from . import views

urlpatterns = [
    
    path('cataract/',views.cataract,name='cataract'),
    path('corneal/',views.corneal,name='corneal'),
    path('glaucoma/',views.Glaucoma,name='glaucoma'),
    path('diabetic/',views.diabetic_retinopathy,name='diabetic'),
    
    
]