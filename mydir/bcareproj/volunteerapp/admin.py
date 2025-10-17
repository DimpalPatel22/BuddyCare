from django.contrib import admin
from .models import Volunteer
from .models import VolunteerGroupRequest
# Register your models here.

@admin.register(Volunteer)
class VolunteerAdmin(admin.ModelAdmin):
    list_display = ('name', 'volunteer_type', 'contact', 'email','location')
    search_fields = ('name', 'volunteer_type', 'location')

@admin.register(VolunteerGroupRequest)
class VolunteerGroupRequestAdmin(admin.ModelAdmin):
    list_display = ('name', 'group', 'contact', 'submitted_at')