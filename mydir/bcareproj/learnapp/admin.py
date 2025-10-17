from django.contrib import admin
from .models import UserTips

# Register your models here.
@admin.register(UserTips)
class UserTipsAdmin(admin.ModelAdmin):
    list_display = ('username', 'tip_type', 'status', 'submitted_at')
    list_filter = ('tip_type', 'status')
    search_fields = ('username', 'tip_text')
    actions = ['approve_tips', 'reject_tips']

    def approve_tips(self, request, queryset):
        updated = queryset.update(status='approved')
        self.message_user(request, f"{updated} tip(s) marked as approved.")
    approve_tips.short_description = "Approve selected tips"

    def reject_tips(self, request, queryset):
        updated = queryset.update(status='rejected')
        self.message_user(request, f"{updated} tip(s) marked as rejected.")
    reject_tips.short_description = "Reject selected tips"