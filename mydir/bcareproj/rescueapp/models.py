from django.db import models
from django.conf import settings
from volunteerapp.models import Volunteer

# Create your models here.
class RescueRequest(models.Model):
    ANIMAL_CHOICES = [
        ('Dog','Dog'),('Cat','Cat'),('Bird','Bird'),('Cow','Cow'),('Other','Other')
    ]
    CONDITION_CHOICES = [
        ('Injured','Injured'),('Sick','Sick'),('Starving','Starving'),
        ('Abandoned','Abandoned'),('Trapped','Trapped'),('Other','Other')
    ]
    STATUS_CHOICES = [
        ('pending','Pending'),
        ('assigned','Assigned'),
        ('in_progress','In Progress'),
        ('resolved','Resolved'),
        ('closed','Closed'),
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL, related_name='reports')
    animal_type = models.CharField(max_length=32, choices=ANIMAL_CHOICES)
    condition = models.CharField(max_length=32, choices=CONDITION_CHOICES)
    location = models.TextField()
    contact = models.CharField(max_length=50, blank=True)
    notes = models.TextField(blank=True)
    image = models.ImageField(upload_to='rescues/')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    assigned_volunteer = models.ForeignKey(
        Volunteer, 
        null=True, 
        blank=True, 
        on_delete=models.SET_NULL,
        related_name='assigned_rescues'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.animal_type} — {self.condition} — {self.location[:40]}"