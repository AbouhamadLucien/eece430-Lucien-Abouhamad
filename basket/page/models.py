

# Create your models here.
from django.db import models

class User(models.Model):
    username=models.CharField(max_length=50,default='')
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()
    gender = models.CharField(max_length=10)
    skill_level = models.CharField(max_length=20)
    password = models.CharField(max_length=100)

class Coach(models.Model):
    username=models.CharField(max_length=30,default='')
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField(max_length=50)
    gender = models.CharField(max_length=10)
    password = models.CharField(max_length=50)
    experience = models.CharField(max_length=400)
    resume = models.FileField(upload_to='resumes/')