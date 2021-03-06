# Generated by Django 3.2.7 on 2021-10-09 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_alter_medicinedetail_location'),
    ]

    operations = [
        migrations.CreateModel(
            name='PatientDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('patient_name', models.CharField(max_length=300)),
                ('age', models.IntegerField(blank=True, default=0, null=True)),
                ('gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Not Mentioned')], max_length=8)),
                ('contact_no', models.CharField(blank=True, max_length=15, null=True)),
                ('patient_type', models.CharField(choices=[('new', 'New'), ('old', 'Old'), ('other', 'Do not know')], max_length=10)),
                ('clinic_info', models.CharField(blank=True, choices=[('pamplet', 'Newspaper'), ('online1', 'Practo'), ('online2', 'Google'), ('online3', 'Facebook'), ('online4', 'Instagram'), ('recommended', 'Recommended'), ('hoarding', 'Hoarding'), ('others', 'Others')], max_length=20, null=True)),
                ('disease', models.CharField(blank=True, max_length=300, null=True)),
                ('symptoms', models.CharField(blank=True, max_length=300, null=True)),
                ('prescription', models.CharField(blank=True, max_length=500, null=True)),
            ],
        ),
    ]
