# Generated by Django 4.2.4 on 2023-11-05 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emp', '0002_emp_department_alter_emp_working'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emp',
            name='emp_id',
            field=models.IntegerField(),
        ),
    ]
