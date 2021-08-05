from django.shortcuts import render

from .forms import  ViewAvailableCourse
# Create your views here.
def view_course(request):
       if request.method=="POST":
           form=ViewAvailableCourse(request.POST)
           if form.is_valid():
               form.save()
           else:
               print(form.errors)    
       else:
            form=ViewAvailableCourse()
       return render (request,"view_course.html",{"form":form})
           
