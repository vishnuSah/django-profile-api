from django.db import models

# Create your models here.

choices = (('ME','Mechanical Engg'), ('CS','Computer Science'), ('EE','Electrical Engg'))
class Emp(models.Model):
    name = models.CharField(max_length=20)
    emp_id = models.IntegerField(null=True)
    phone = models.CharField(max_length=10,null=True)
    address = models.TextField(null=True)
    working = models.BooleanField(default=False)
    department = models.CharField(max_length=20, choices=choices, null=True)