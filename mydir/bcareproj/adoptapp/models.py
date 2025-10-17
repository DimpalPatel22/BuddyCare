from django.db import models

# Create your models here.
class AdoptionRequest(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    pet_name = models.CharField(max_length=100)
    reason = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        max_length=20,
        choices=[('Pending', 'Pending'), ('In Progress', 'In Progress'), ('Completed', 'Completed')],
        default='Pending'
    )

    def __str__(self):
        return f"{self.name} - {self.pet_name}"
    
    class Meta:
        verbose_name = "Adoption Request"
        verbose_name_plural = "Adoption Requests"
        app_label = "rescueapp"  # <--- this makes it appear under Rescueapp in admin
