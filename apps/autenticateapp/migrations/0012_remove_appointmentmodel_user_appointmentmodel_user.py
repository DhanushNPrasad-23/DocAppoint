# Generated by Django 5.1 on 2024-10-24 06:53

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('autenticateapp', '0011_remove_appointmentmodel_ap_id_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appointmentmodel',
            name='user',
        ),
        migrations.AddField(
            model_name='appointmentmodel',
            name='user',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
