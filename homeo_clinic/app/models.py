from django.db import models


class MedicineDetail(models.Model):

    medicine_brand_choice = (
        ('reckeweg', 'Reckeweg'),
        ('sbl', 'SBL'),
        ('schwabe', 'Schwabe'),
        ('bakson', 'Bakson'),
        ('bhargawa', 'Bhargawa'),
    )

    strength_choice = (
        ('Combination', 'Combination'),
        ('ExternalUse', 'External Use'),
        ('Syrup', 'Syrup'),
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

    location_choice = (
        ('r1-a', 'R1-A'),
        ('r1-b', 'R1-B'),
        ('r1-c', 'R1-C'),
        ('r1-d', 'R1-D'),
        ('r2-a', 'R2-A'),
        ('r2-b', 'R2-B'),
        ('r2-c', 'R2-C'),
        ('r2-d', 'R2-D'),
    )

    medicine_name = models.CharField(max_length=100, unique=True)
    medicine_brand = models.CharField(max_length=100, choices=medicine_brand_choice)
    strength = models.CharField(max_length=50, null=True, choices=strength_choice)
    in_stock = models.CharField(max_length=10, null=True, choices=in_stock_choice)
    location = models.CharField(max_length=6, blank=True, null=True, choices=location_choice)
    quantity = models.CharField(max_length=6, default='', blank=True, null=True)
    count = models.IntegerField(default=0, blank=True, null=True)
    mrp = models.CharField(max_length=10, default='', blank=True, null=True)
    spr = models.CharField(max_length=10, default='', blank=True, null=True)
    therapeutic_use = models.TextField(max_length=500, default='', blank=True, null=True)
    symptom = models.TextField(max_length=1000, default='', blank=True, null=True)


class PatientDetail(models.Model):

    gender_choices = (
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Not Mentioned'),
    )

    patient_type_choices = (
        ('new', 'New'),
        ('old', 'Old'),
        ('fup', 'FUP'),
    )

    clinic_info_choices = (
        ('pamplet', 'Newspaper'),
        ('online1', 'Practo'),
        ('online2', 'Google'),
        ('online3', 'Facebook'),
        ('online4', 'Instagram'),
        ('recommended', 'Recommended'),
        ('hoarding', 'Hoarding'),
        ('walk-in', 'WalkIn'),
    )

    date = models.DateField()
    patient_name = models.CharField(max_length=300)
    age = models.IntegerField(default=0, blank=True, null=True)
    gender = models.CharField(max_length=8, choices=gender_choices)
    contact_no = models.CharField(max_length=15, blank=True, null=True)
    patient_type = models.CharField(max_length=10, choices=patient_type_choices)
    clinic_info = models.CharField(max_length=20, blank=True, null=True, choices=clinic_info_choices)
    disease = models.TextField(max_length=500, blank=True, null=True)
    symptoms = models.TextField(max_length=500, blank=True, null=True)
    past_history = models.TextField(max_length=500, blank=True, null=True)
    family_history = models.TextField(max_length=500, blank=True, null=True)
    generalities = models.TextField(max_length=500, blank=True, null=True)
    on_examination = models.TextField(max_length=500, blank=True, null=True)
    lab_reports = models.TextField(max_length=500, blank=True, null=True)
    prescription = models.TextField(max_length=1000, blank=True, null=True)
    advice = models.TextField(max_length=500, blank=True, null=True)
    consultation = models.IntegerField(default=0, blank=True, null=True)
    medicine_fee = models.IntegerField(default=0, blank=True, null=True)
