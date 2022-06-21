# Generated by Django 4.0.4 on 2022-06-08 03:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department_name', models.CharField(max_length=225)),
                ('department_image', models.ImageField(null=True, upload_to='image/')),
                ('department_images', models.ImageField(null=True, upload_to='image/')),
            ],
        ),
        migrations.CreateModel(
            name='doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.TextField(max_length=100)),
                ('specilisation', models.CharField(max_length=100)),
                ('image', models.ImageField(null=True, upload_to='image/')),
                ('qualification', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=12)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='designation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('designation', models.TextField(max_length=100)),
                ('department', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='healthApp.department')),
                ('doctor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='healthApp.doctor')),
            ],
        ),
    ]