# Generated by Django 3.2.7 on 2021-10-09 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_alter_patientdetail_patient_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='patientdetail',
            name='consultation',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='patientdetail',
            name='medicine_fee',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
