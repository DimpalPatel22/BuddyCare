from django.contrib import admin
from .models import RescueRequest
# Register your models here.

@admin.register(RescueRequest)
class RescueRequestAdmin(admin.ModelAdmin):
    list_display = ('id','animal_type','condition','status','assigned_volunteer','created_at')
    list_filter = ('animal_type','condition','status','created_at')
    search_fields = ('location','notes','contact')
    readonly_fields = ('created_at','updated_at')

    # Allow editing directly in the list view
    list_editable = ('status', 'assigned_volunteer')