from django.db import models
from django.contrib.auth.models import User

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class Donation(models.Model):
    DONATION_TYPE_CHOICES = [
        ('online', 'Online'),
        ('offline', 'Offline'),
    ]
    ONLINE_METHOD_CHOICES = [
        ('UPI', 'UPI'),
        ('Card', 'Credit/Debit Card'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=100)
    contact = models.CharField(max_length=20, blank=True)
    donation_type = models.CharField(max_length=10, choices=DONATION_TYPE_CHOICES)
    online_method = models.CharField(max_length=10, choices=ONLINE_METHOD_CHOICES, blank=True, null=True) 
    amount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    item = models.CharField(max_length=200, blank=True)  # For offline donations
    notes = models.TextField(blank=True)
    expiry_confirm = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.donation_type} - {self.created_at.strftime('%Y-%m-%d')}"
