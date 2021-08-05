from django.db import models
from django.db.models.fields import CharField, DurationField
from django.http import request
# Create your models here.

class Trainer(models.Model):
    first_name=models.CharField(max_length=10)
    last_name=models.CharField(max_length=10)
    title=models.CharField(max_length=10)
    course=models.CharField(max_length=10)
    unit=models.CharField(max_length=10)
    duration=models.DurationField()
    email=models.EmailField()
    bank_account_no=models.CharField(max_length=20)
    phone_number=models.CharField(max_length=20)
    profession=models.CharField(max_length=20)
    company=models.CharField(max_length=20)
    job_title=models.CharField(max_length=10)
    lessons_attendance=models.PositiveSmallIntegerField()
    resume=models.FileField()
    nat=((u'R',U'Rwandese'),
                (u'K',u'Kenyan'),
                (u'Su',u'Sudanesse'),
                (u'S','Somali'),
                (u'SS','South Sudanese')



    )
    nationality=models.CharField(max_length=20,choices=nat)
    lessons_per_month=models.PositiveSmallIntegerField()
    contract=models.FileField()
    syllabus=models.FileField()
    id_number=models.PositiveSmallIntegerField()