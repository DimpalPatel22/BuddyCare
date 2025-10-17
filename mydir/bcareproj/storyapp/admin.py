from django.contrib import admin
from .models import Story

# Register your models here.
@admin.register(Story)
class StoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'storyteller', 'user', 'status', 'created_at')
    list_filter = ('status', 'created_at')
    search_fields = ('title', 'storyteller', 'content', 'user__username')
    actions = ['approve_stories', 'reject_stories']

    def approve_stories(self, request, queryset):
        updated = queryset.update(status='approved')
        self.message_user(request, f"{updated} story(ies) marked as approved.")
    approve_stories.short_description = "Approve selected stories"

    def reject_stories(self, request, queryset):
        updated = queryset.update(status='rejected')
        self.message_user(request, f"{updated} story(ies) marked as rejected.")
    reject_stories.short_description = "Reject selected stories"