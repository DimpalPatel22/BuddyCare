from django.contrib import admin
from .models import AdoptionRequest

# Register your models here.
@admin.register(AdoptionRequest)
class AdoptionRequestAdmin(admin.ModelAdmin):
    list_display = ('name', 'pet_name', 'email', 'phone', 'status', 'submitted_at')
    list_filter = ('status', 'submitted_at')
    search_fields = ('name', 'pet_name', 'email')
    # Optional: custom ordering
    ordering = ('-submitted_at',)