from django.db import models
from django.db.models.fields import DateField

# Create your models here.
class Student(models.Model):
    first_name=models.CharField(max_length=10)
    last_name=models.CharField(max_length=10)
    age=models.PositiveSmallIntegerField() 
    date_of_birth=models.DateField()

    