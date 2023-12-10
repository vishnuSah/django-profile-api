from django.urls import path, include
from . import views

urlpatterns = [
    path('index/', views.home, name='index'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
]

