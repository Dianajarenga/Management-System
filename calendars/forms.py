from django import forms
from django.db.models.base import Model
from .models import Calendar

class ViewCalendar(forms.ModelForm):
    class Meta:
        model=Calendar
        fields="__all__"
