# Generated by Django 4.2.4 on 2023-11-05 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='emp',
            name='department',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='emp',
            name='working',
            field=models.BooleanField(default=False),
        ),
    ]
