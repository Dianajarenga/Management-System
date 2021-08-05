
from django.urls import path
from django.conf import settings
from .views import trainer_register
from django.conf.urls.static import static

urlpatterns=[
    path("register/",trainer_register,name="Register Trainer"),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)