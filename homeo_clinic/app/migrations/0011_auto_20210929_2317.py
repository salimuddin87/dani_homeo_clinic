# Generated by Django 3.2.7 on 2021-09-29 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_auto_20210929_2310'),
    ]

    operations = [
        migrations.AddField(
            model_name='medicinedetail',
            name='count',
            field=models.CharField(blank=True, default='', max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='medicinedetail',
            name='quantity',
            field=models.CharField(blank=True, default='', max_length=6, null=True),
        ),
    ]
