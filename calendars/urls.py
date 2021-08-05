from django.urls import path
from .views import view_calendars

urlpatterns=[
    path("register/",view_calendars,name="View Calendar"),
]