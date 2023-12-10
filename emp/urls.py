from django.urls import path, include
from emp.views import *

urlpatterns = [
   path('home/', emp_home, name='home'),
   path('add_emp/', add_emp, name='add_emp'),
   path('delete-emp/<int:emp_id>', delete_emp, name='delete-emp'),
   path('update-emp/<int:emp_id>', update_emp, name='update-emp'),
]
