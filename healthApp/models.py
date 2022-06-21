
import email
from django.db import models
from django.contrib.auth.models import User

# Create your models here.




class doctor(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE ,null=True)
    address = models.TextField(max_length=100)
    specilisation = models.CharField(max_length=100)    
    image = models.ImageField(upload_to="image/", null=True)
    qualification= models.CharField(max_length=100)  
    phone=models.CharField(max_length=12)
   
  
class department(models.Model):
    department_name = models.CharField(max_length=225)
    department_image=models.ImageField(upload_to="image/", null=True)
    department_images=models.ImageField(upload_to="image/", null=True)
   



class designation(models.Model):
    doctor = models.ForeignKey(doctor,on_delete=models.CASCADE ,null=True)
    department=models.ForeignKey(department,on_delete=models.CASCADE,null=True)
    designation=models.TextField(max_length=100)

    

    

   

class appoinment(models.Model):
    name= models.CharField(max_length=225)
    address= models.CharField(max_length=225)
    gender= models.CharField(max_length=225)
    age= models.IntegerField()
    phone= models.CharField(max_length=225)
    bloodgroup= models.CharField(max_length=225)
    doctor=models.ForeignKey(designation,on_delete=models.CASCADE,null=True)
    email=models.EmailField()
   

