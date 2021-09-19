from django.db import models


class MedicineDetail(models.Model):
    medicine_code = models.CharField(max_length=100)
    medicine_name = models.CharField(max_length=100)
    medicine_brand = models.CharField(max_length=100)
    date_of_mfg = models.DateField()
    date_of_exp = models.DateField(blank=True, null=True)
