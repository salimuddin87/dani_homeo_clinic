from django.db import models


class MedicineDetail(models.Model):
    medicine_code = models.CharField(max_length=100)
    medicine_name = models.CharField(max_length=100)
    medicine_brand = models.CharField(max_length=100)
    strength = models.CharField(max_length=100, null=True)
    in_stock = models.CharField(max_length=100, null=True)
    therapeutic_use = models.CharField(max_length=500, default='', blank=True, null=True)
    symptom = models.CharField(max_length=500, default='', blank=True, null=True)
    date_of_mfg = models.DateField(blank=True, null=True)
    date_of_exp = models.DateField(blank=True, null=True)
