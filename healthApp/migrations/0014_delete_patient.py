# Generated by Django 4.0.4 on 2022-06-08 10:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('healthApp', '0013_appoinment'),
    ]

    operations = [
        migrations.DeleteModel(
            name='patient',
        ),
    ]