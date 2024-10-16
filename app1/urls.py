from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('', views.tatuadores, name='tatuadores'),
    path('', views.galeria, name='galeria'),
    path('', views.contacto, name='contacto'),
]    




