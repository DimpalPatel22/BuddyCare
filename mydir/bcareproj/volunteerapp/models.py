from django.db import models

# Create your models here.
class Volunteer(models.Model):
    VOLUNTEER_TYPES = [
        ('Street Rescuer', 'Street Rescuer'),
        ('Adoption Support', 'Adoption Support'),
        ('Bird Rescuer', 'Bird Rescuer'),
        ('Feeding Volunteer', 'Feeding Volunteer'),
        ('Medical Support', 'Medical Support'),
        ('Community Educator', 'Community Educator'),
        ('Pet Caretaker', 'Pet Caretaker'),
    ]

    name = models.CharField(max_length=100)
    contact = models.CharField(max_length=20)
    email = models.EmailField(blank=True, null=True)
    volunteer_type = models.CharField(max_length=50, choices=VOLUNTEER_TYPES)
    location = models.CharField(max_length=100, blank=True)
    experience_years = models.IntegerField(default=0)
    skills = models.TextField(blank=True)

    def __str__(self):
        return f"{self.name} ({self.volunteer_type})"

class VolunteerGroupRequest(models.Model):
    GROUP_CHOICES = [
        ('street_feeding', 'Street Feeding Crew'),
        ('bird_rescue', 'Bird Rescue Team'),
        ('adoption_support', 'Adoption Support Squad'),
    ]

    name = models.CharField(max_length=100)
    contact = models.CharField(max_length=20)
    group = models.CharField(max_length=50, choices=GROUP_CHOICES)
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.get_group_display()}"
