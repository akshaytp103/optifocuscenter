from django.db import models

# Create your models here.
class Service(models.Model):
    name = models.CharField(max_length=20,null=True)
    Heading=models.CharField(max_length=50)
    content = models.TextField(max_length=10000)
    subcontents = models.CharField(max_length=1000)
    images = models.ImageField(upload_to='contentphoto',null=True,blank=True)
    
    def __str__(self):
        return self.name
