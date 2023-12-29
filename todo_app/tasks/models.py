from django.db import models
from datetime import datetime

# Create your models here.

class Task(models.Model):
    name = models.CharField(max_length=200)
    completed = models.BooleanField()
    created_at = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.name

