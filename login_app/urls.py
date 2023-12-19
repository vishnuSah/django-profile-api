from django.urls import path
from . import views

urlpatterns = [
    path('', views.render_login, name='render_login'),
    path('perform_login', views.perform_login, name='perform_login'),
    path('admin_dashboard', views.admin_dashboard, name='admin_dashboard'),
    path('perform_register', views.perform_register, name='perform_register'),
    path('perform_logout', views.perform_logout, name='perform_logout'),
]