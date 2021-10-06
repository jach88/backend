from django.conf.urls import url
from django.urls import path
from django.urls.resolvers import URLPattern
from .views import ComprobanteController

urlpatterns = [
    path('generar-comprobante/', ComprobanteController.as_view()) 
]
