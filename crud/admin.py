from django.contrib import admin
from .models import students

# Register your models here.
class studentsAdmin(admin.ModelAdmin):
    list_display = ('stud_id','name','standard','roll_no','address')

admin.site.register(students, studentsAdmin)
