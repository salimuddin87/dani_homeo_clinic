# Generated by Django 3.2.7 on 2021-09-19 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20210919_1306'),
    ]

    operations = [
        migrations.AddField(
            model_name='medicinedetail',
            name='in_stock',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='medicinedetail',
            name='strength',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='medicinedetail',
            name='symptom',
            field=models.CharField(default=None, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='medicinedetail',
            name='therapeutic_use',
            field=models.CharField(default=None, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='medicinedetail',
            name='date_of_mfg',
            field=models.DateField(blank=True, null=True),
        ),
    ]
