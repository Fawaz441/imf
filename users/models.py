from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()
# Create your models here.



class Student(models.Model):
    user = models.OneToOneField(User,related_name='student',on_delete=models.CASCADE)
    location = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=20)

    class Meta:
        verbose_name = 'Student'

class Farmer(models.Model):
    user = models.OneToOneField(User,related_name='farmer',on_delete=models.CASCADE)
    land_size = models.CharField(max_length=20)
    location = models.CharField(max_length=300)
    farm_name = models.CharField(max_length=200,null=True,blank=True)
    does_livestock = models.BooleanField(default=False)
    major_products = models.CharField(max_length=200)

    class Meta:
        verbose_name = 'Farmer'

class Company(models.Model):
    user = models.OneToOneField(User,related_name='company',on_delete=models.CASCADE)
    company_name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=20)
    
    class Meta:
        verbose_name = 'Companie'

    
class Challenger(models.Model):
    email = models.EmailField()
    
    def __str__(self):
        return self.email


