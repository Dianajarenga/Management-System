from django.db import models
from django.db.models.fields import DurationField
class Course(models.Model):
    course_title=models.CharField(max_length=10)
    unit=models.CharField(max_length=10)
    duration=models.DurationField()
# Create your models here.
