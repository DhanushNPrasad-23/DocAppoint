from django.db import models
import uuid
from django.contrib.auth.models import User
# Create your models here.


class DisplayModel(models.Model):
    name = models.CharField(max_length=20,blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    
    def __str__(self) -> str:
        return self.name







class DoctorModel(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=12,blank=True, null=True)
    email = models.CharField( max_length=50 , blank=True, null=True)
    specialization = models.CharField(max_length=50,blank=True, null=True)
    def __str__(self) -> str:
        return self.user.username
    
    
class PatientModel(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    p_id = models.CharField(max_length=40)
    address = models.CharField(max_length=100,blank=True, null=True)
    email = models.CharField(max_length=50,blank=True, null=True)
    p_pno = models.CharField(max_length=15,blank=True, null=True)
    def __str__(self) -> str:
        return self.user.username

class AppointmentModel(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    pat_name = models.CharField(max_length=40,blank=True, null=True)
    appointment_date  = models.CharField(max_length=30)
    doc_name = models.CharField(max_length=100)
    email = models.CharField(max_length=50,blank=True, null=True)
    age = models.CharField(max_length=30,blank=True, null=True)
    gender = models.CharField(max_length=10,blank=True, null=True)
    description = models.TextField(max_length=300,blank=True, null=True)
    
    def __str__(self) -> str:
        return self.pat_name
    
    