from django.db import models
from django.db.models.fields import CharField, DurationField

# Create your models here.

class Trainer(models.Model):
    first_name=models.CharField(max_length=10)
    last_name=models.CharField(max_length=10)
    title=models.CharField(max_length=10)
    course=models.CharField(max_length=10)
    unit=models.CharField(max_length=10)
    duration=models.DurationField()


