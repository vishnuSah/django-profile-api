from django.urls import path, include
from . import views

urlpatterns = [
    path('index/', views.index),
    path('get_students/', views.get_students),
    path('add_student/', views.add_student),
    path('delete_student/<int:stud_id>', views.delete_student),
    path('update_student/<int:stud_id>', views.update_student),
    path('search_student/', views.search_student, name="search_student"),
]