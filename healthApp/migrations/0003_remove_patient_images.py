# Generated by Django 4.0.4 on 2022-06-08 04:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('healthApp', '0002_patient'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient',
            name='images',
        ),
    ]
