from django.db import models
from django.db.models.fields import DateTimeField
from django.http import request

class Calendar(models.Model):
    event_name=models.CharField(max_length=20)
    event_date=models.DateTimeField()
    event_agenda=models.CharField(max_length=30)
    event_duration=models.DurationField()
    event_planner=models.CharField(max_length=10)
    event_venue=models.CharField(max_length=10)
    number_of_event_attendees=models.BigIntegerField()
    event_activity=models.CharField(max_length=10)
    event_approved_by=models.CharField(max_length=20)




# Create your models here.
