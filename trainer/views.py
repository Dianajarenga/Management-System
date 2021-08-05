from .forms import TrainerRegistrationForm
from django.shortcuts import render
def trainer_register(request):
       if request.method=="POST":
           form=TrainerRegistrationForm(request.POST)
           if form.is_valid():
               form.save()
           else:
               print(form.errors)    
       else:
            form=TrainerRegistrationForm()
       return render (request,"trainer_register.html",{"form":form})
           

# Create your views here.
