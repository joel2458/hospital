# Generated by Django 4.0.4 on 2022-06-08 08:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('healthApp', '0008_patient_department_patient_doctor'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient',
            name='department',
        ),
    ]
