from django.db import models


class MedicineDetail(models.Model):

    medicine_brand_choice = (
        ('reckeweg', 'Reckeweg'),
        ('sbl', 'SBL'),
        ('schwabe', 'Schwabe'),
    )

    strength_choice = (
        ('Mother', 'Mother'),
        ('CM', 'CM'),
        ('10M', '10M'),
        ('1M', '1M'),
        ('200', '200'),
        ('30', '30'),
        ('12', '12'),
        ('6x', '6X'),
        ('3x', '3X'),
    )

    in_stock_choice = (
        ('yes', 'YES'),
        ('no', 'NO'),
    )

    medicine_name = models.CharField(max_length=100)
    medicine_brand = models.CharField(max_length=100, choices=medicine_brand_choice)
    strength = models.CharField(max_length=100, null=True, choices=strength_choice)
    in_stock = models.CharField(max_length=100, null=True, choices=in_stock_choice)
    therapeutic_use = models.CharField(max_length=500, default='', blank=True, null=True)
    symptom = models.CharField(max_length=500, default='', blank=True, null=True)
    date_of_mfg = models.DateField(blank=True, null=True)
    date_of_exp = models.DateField(blank=True, null=True)
