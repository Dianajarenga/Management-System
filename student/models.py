from django.db import models
from django.db.models.fields import BigAutoField, CharField, DateField, EmailField

# Create your models here.
class Student(models.Model):
    First_name=models.CharField(max_length=10)
    Last_name=models.CharField(max_length=10)
    Age=models.PositiveSmallIntegerField() 
    Date_of_birth=models.DateField()
    Gend=((u'=M',U'Male'),
                (u'K',u'Female'),
                (u'O',u'Other'))

    Gender=models.CharField(max_length=20,choices=Gend)
    Email=models.EmailField()
    Lang=((u'E',U'English'),
                (u'K',u'Kiswahili'),
                (u'O',u'Other')


    )
    Languages=  models.CharField(max_length=2 ,choices=Lang)
    ID_number=models.CharField(max_length=10)
    
    Nationality=models.CharField(max_length=20)
    Passport_photo=models.ImageField()
    Phone_number=models.PositiveIntegerField()
    Room_number=models.PositiveSmallIntegerField()
    Mentors_name=models.CharField(max_length=20)
    Class_name=models.CharField(max_length=10)
    Medical_report=models.FileField()
    Laptop_serial=models.CharField(max_length=10)
    Big_sister=models.CharField(max_length=20)
    Passport_number=models.CharField(max_length=10)
    Guardian=models.CharField(max_length=20)
    District=models.CharField(max_length=20)


    






