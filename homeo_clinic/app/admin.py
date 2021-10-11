from django.contrib import admin

from .models import MedicineDetail, PatientDetail


class MedicineAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['medicine_name']}),
        (None, {'fields': ['medicine_brand']}),
        (None, {'fields': ['strength']}),
        (None, {'fields': ['in_stock']}),
        (None, {'fields': ['location']}),
        (None, {'fields': ['quantity']}),
        (None, {'fields': ['count']}),
        (None, {'fields': ['mrp']}),
        (None, {'fields': ['spr']}),
        (None, {'fields': ['therapeutic_use']}),
        (None, {'fields': ['symptom']}),
    ]
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

    list_filter = ['medicine_brand', 'in_stock', 'strength']

    search_fields = ['medicine_name', 'therapeutic_use', 'symptom']

    sortable_by = ['medicine_name', 'medicine_brand', 'strength', 'in_stock']

    list_per_page = 5


class PatientAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['date']}),
        (None, {'fields': ['patient_name']}),
        (None, {'fields': ['age']}),
        (None, {'fields': ['gender']}),
        (None, {'fields': ['contact_no']}),
        (None, {'fields': ['patient_type']}),
        (None, {'fields': ['clinic_info']}),
        (None, {'fields': ['disease']}),
        (None, {'fields': ['symptoms']}),
        (None, {'fields': ['prescription']}),
        (None, {'fields': ['consultation']}),
        (None, {'fields': ['medicine_fee']}),
    ]
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
        'prescription',
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

    list_per_page = 10


admin.site.register(MedicineDetail, MedicineAdmin)
admin.site.register(PatientDetail, PatientAdmin)
