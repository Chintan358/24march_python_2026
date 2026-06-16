from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=25)
    email = models.CharField(max_length=50)
    age = models.IntegerField()
    phone = models.CharField(max_length=20,null=True)
    dept = models.CharField(max_length=15,null=True)
    subject = models.CharField(max_length=20,default='Python')
    