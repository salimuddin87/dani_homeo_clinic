from django.contrib import admin

from .models import MedicineDetail, PatientDetail


class MedicineAdmin(admin.ModelAdmin):
    fields = (
        ('medicine_name', 'medicine_brand'),
        ('strength', 'in_stock', 'location'),
        ('quantity', 'count'),
        ('mrp', 'spr'),
        'therapeutic_use',
        'symptom',
    )

    list_display = (
        'medicine_name',
        'medicine_brand',
        'strength',
        'in_stock',
        'location',
        'quantity',
        'count',
        'mrp',
        'spr',
        'therapeutic_use',
        'symptom',
    )

    # list_filter = ['medicine_brand', 'in_stock']

    search_fields = ['medicine_name', 'therapeutic_use', 'symptom']

    sortable_by = ['medicine_name', 'medicine_brand', 'strength', 'in_stock']

    list_per_page = 5


class PatientAdmin(admin.ModelAdmin):
    fields = (
        ('date', 'patient_name'),
        ('age', 'gender', 'contact_no'),
        ('patient_type', 'clinic_info'),
        'disease',
        'symptoms',
        'past_history',
        'family_history',
        'generalities',
        'on_examination',
        'lab_reports',
        'prescription',
        'advice',
        ('consultation', 'medicine_fee'),
    )

    list_display = (
        'date',
        'patient_name',
        'age',
        'gender',
        'contact_no',
        'patient_type',
        'clinic_info',
        'disease',
        'symptoms',
        'past_history',
        'family_history',
        'generalities',
        'on_examination',
        'lab_reports',
        'prescription',
        'advice',
        'consultation',
        'medicine_fee',
    )

    search_fields = [
        'date',
        'patient_name',
        'age',
        'gender',
        'contact_no',
        'patient_type',
        'clinic_info',
        'disease',
        'symptoms',
        'prescription',
    ]

    sortable_by = ['date', 'patient_name', 'age', 'gender', 'disease']

    list_per_page = 5


admin.site.register(MedicineDetail, MedicineAdmin)
admin.site.register(PatientDetail, PatientAdmin)
