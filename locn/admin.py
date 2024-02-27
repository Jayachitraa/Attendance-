from django.contrib import admin
from .models import AttLocnMast, AttMastGatTat, AttDetGatTat

@admin.register(AttLocnMast)
class AttLocnMastAdmin(admin.ModelAdmin):
    list_display = ['locn_code', 'locn_name']
    search_fields = ['locn_code', 'locn_name']

@admin.register(AttMastGatTat)
class AttMastGatTatAdmin(admin.ModelAdmin):
    list_display = ['empno', 'locn_cd', 'zone', 'dept', 'status']
    search_fields = ['empno', 'locn_cd__locn_code', 'zone', 'dept', 'status']
    list_filter = ['status']

@admin.register(AttDetGatTat)
class AttDetGatTatAdmin(admin.ModelAdmin):
    list_display = ['empno', 'name', 'att_dt', 'att_typ']
    search_fields = ['empno__empno', 'name', 'att_dt', 'att_typ']
    list_filter = ['att_typ']

# You can customize the admin classes further based on your requirements
