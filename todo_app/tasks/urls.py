from django.urls import path, include
from .views import index, update, delete

urlpatterns = [
   path('', index, name='list'),
   path('update/<str:pk>', update, name='update'),
   path('delete/<str:pk>', delete, name='delete')
]