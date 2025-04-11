from django.db import models

class LocationRequest(models.Model):
    location = models.CharField(max_length=255)
    country = models.CharField(max_length=100)
    state = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    user_name = models.CharField(max_length=100, blank=True, null=True)
    user_email = models.EmailField(blank=True, null=True)
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.location} ({self.country})"
