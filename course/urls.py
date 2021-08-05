from django.urls import path
from .views import view_course

urlpatterns=[
    path("register/",view_course,name="View Courses"),
]