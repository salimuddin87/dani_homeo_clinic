from django.contrib import admin

from .models import MedicineDetail


class MedicineAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['medicine_name']}),
        (None, {'fields': ['medicine_brand']}),
        (None, {'fields': ['strength']}),
        (None, {'fields': ['in_stock']}),
        (None, {'fields': ['therapeutic_use']}),
        (None, {'fields': ['symptom']}),
        (None, {'fields': ['date_of_mfg']}),
        (None, {'fields': ['date_of_exp']}),
    ]
    list_display = (
        'medicine_name',
        'medicine_brand',
        'strength',
        'in_stock',
        'therapeutic_use',
        'symptom',
        'date_of_mfg',
        'date_of_exp',
    )

    list_filter = ['medicine_brand']

    search_fields = ['medicine_name','therapeutic_use', 'symptom']

    sortable_by = ['medicine_name', 'medicine_brand', 'strength', 'in_stock', 'date_of_mfg', 'date_of_exp']


admin.site.register(MedicineDetail, MedicineAdmin)
