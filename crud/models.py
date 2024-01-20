from django.db import models

# Create your models here.
class students(models.Model):
    stud_id = models.IntegerField(unique=True)
    name = models.CharField(max_length=30)
    standard = models.IntegerField()
    roll_no = models.IntegerField()
    address = models.CharField(max_length=30)



