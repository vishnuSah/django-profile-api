from django.contrib import admin
from .models import Task

# Register your models here.

class TaskAdmin(admin.ModelAdmin):
    model = Task
    list_display = ('name','completed','created_at')

admin.site.register(Task, TaskAdmin)
