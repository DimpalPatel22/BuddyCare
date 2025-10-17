from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserTips(models.Model):
    CATEGORY_CHOICES = [
        ('food', 'Food & Nutrition'),
        ('remedies', 'Remedies'),
        ('disease', 'Disease & Health Awareness'),
        ('other', 'Other'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="user_tips")
    username = models.CharField(max_length=100)
    email = models.EmailField(blank=True, null=True)
    tip_type = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    other_text = models.CharField(max_length=200, blank=True, null=True)
    tip_text = models.TextField(blank=True, null=True)
    submitted_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        max_length=20,
        choices=[('pending', 'Pending'), ('approved', 'Approved'), ('rejected', 'Rejected')],
        default='pending'
    )
    approved = models.BooleanField(default=False)

    class Meta:
        app_label = "storyapp"   # forces it to show under Storyapp in admin
        verbose_name = "User Tip"

    def __str__(self):
        return f"{self.username} - {self.tip_type}"