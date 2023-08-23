from django.contrib import admin
from django.urls import path
from api.views import profileView

urlpatterns = [
    path('list/' , profileView.as_view(), name='list'),
    path('save/', profileView.as_view(), name='save')
] 