from django.contrib import admin

from .models import MedicineDetail


class MedicineAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['medicine_code']}),
        (None, {'fields': ['medicine_name']}),
        (None, {'fields': ['medicine_brand']}),
        (None, {'fields': ['date_of_mfg']}),
        (None, {'fields': ['date_of_exp']}),
    ]
    list_display = ('medicine_code', 'medicine_name', 'medicine_brand', 'date_of_mfg', 'date_of_exp')
    list_filter = ['medicine_brand']
    search_fields = ['medicine_code', 'medicine_name']

    @admin.display(
        boolean=True,
        ordering='medicine_name',
        description='Medicine Name'
    )
    def search_medicine(self):
        pass


admin.site.register(MedicineDetail, MedicineAdmin)
