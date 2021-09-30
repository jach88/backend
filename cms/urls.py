from django.conf.urls import url
from django.urls import path
from .views import (RegistroController)

urlpatterns = [
    path('registro', RegistroController.as_view())
]