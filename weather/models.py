from django.db import models

class WeatherSearch(models.Model):
    city = models.CharField(max_length=100, unique=True)
    data = models.JSONField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.city
