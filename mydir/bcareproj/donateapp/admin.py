from django.contrib import admin
from .models import Donation

# Register your models here.
@admin.register(Donation)
class DonationAdmin(admin.ModelAdmin):
    list_display = ('name', 'donation_type', 'online_method', 'amount', 'item', 'user', 'created_at')