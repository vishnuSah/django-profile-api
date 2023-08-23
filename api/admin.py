from django.contrib import admin
from api.models import profile

@admin.register(profile)
class profileAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'department', 'country', 'gender', 'photo', 'resume']
