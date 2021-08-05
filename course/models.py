from django.db import models
from django.db.models.fields import DurationField
from django.http import request

class Course(models.Model):
    course_title=models.CharField(max_length=10)
    unit=models.CharField(max_length=10)
    duration=models.DurationField()
    trainers_name=models.CharField(max_length=20)
    course_syllabus=models.FileField()
    course_material=models.FileField()
# Create your models here.
