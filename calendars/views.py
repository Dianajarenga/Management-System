from django.shortcuts import render
from .forms import  ViewCalendar

def view_calendars(request):
       if request.method=="POST":
           form=ViewCalendar(request.POST)
           if form.is_valid():
               form.save()
           else:
               print(form.errors)    
       else:
            form=ViewCalendar()
       return render (request,"view_calendars.html",{"form":form})
           

# Create your views here.
