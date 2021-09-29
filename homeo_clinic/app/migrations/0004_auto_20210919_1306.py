# Generated by Django 3.2.7 on 2021-09-19 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_medicinedetails_date_of_exp'),
    ]

    operations = [
        migrations.CreateModel(
            name='MedicineDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('medicine_code', models.CharField(max_length=100)),
                ('medicine_name', models.CharField(max_length=100)),
                ('medicine_brand', models.CharField(max_length=100)),
                ('date_of_mfg', models.DateField()),
                ('date_of_exp', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='MedicineDetails',
        ),
    ]