from django.db import models

departments = (('IT', 'IT'), ('Finance', 'Finance'), ('Pharma', 'Pharma'))
genders= [['Male', 'Male'], ['Female', 'Female'], ['Others', 'Others']]

class profile(models.Model):
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
    department = models.CharField(choices=departments, max_length=20)
    country = models.CharField(max_length=15)
    gender =models.CharField(choices=genders, max_length=20)
    photo = models.ImageField(upload_to='img', blank=True)
    resume = models.FileField(upload_to='resume', blank=True)
