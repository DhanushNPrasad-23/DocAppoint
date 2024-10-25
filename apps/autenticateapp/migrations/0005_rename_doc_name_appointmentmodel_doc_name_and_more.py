# Generated by Django 5.1 on 2024-10-16 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('autenticateapp', '0004_patientmodel_email_patientmodel_p_pno'),
    ]

    operations = [
        migrations.RenameField(
            model_name='appointmentmodel',
            old_name='Doc_name',
            new_name='doc_name',
        ),
        migrations.AddField(
            model_name='appointmentmodel',
            name='age',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='appointmentmodel',
            name='description',
            field=models.TextField(blank=True, max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='appointmentmodel',
            name='email',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='appointmentmodel',
            name='gender',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]