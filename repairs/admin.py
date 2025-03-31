from django.contrib import admin
from .models import RepairRequest

@admin.register(RepairRequest)
class RepairRequestAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'device_type', 'created_at', 'is_processed')
    list_filter = ('device_type', 'is_processed', 'created_at')
    search_fields = ('name', 'phone', 'description')
