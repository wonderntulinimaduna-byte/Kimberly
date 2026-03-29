from django.db import models
from django.contrib.auth.models import User

class Report(models.Model):
    CATEGORY_CHOICES = [
        ('water', 'Water Leak'),
        ('electricity', 'Electricity Fault'),
        ('pothole', 'Pothole'),
        ('waste', 'Waste Collection'),
        ('general', 'General'),
    ]
    STATUS_CHOICES = [
        ('received', 'Received'),
        ('in_progress', 'In Progress'),
        ('resolved', 'Resolved'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    description = models.TextField()
    location = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='reports/', blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='received')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.category} - {self.status}"
