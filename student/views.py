from django.shortcuts import render
from .forms import StudentReistrationForm
# Create your views here.

def register_student(request):
    form=StudentReistrationForm
    return render (request,"register_student.html",{"form":form})