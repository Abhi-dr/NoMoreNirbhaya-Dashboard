from django.db import models
from django.utils import timezone

class SOSAlert(models.Model):
    message = models.CharField(max_length=255)  
    timestamp = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.message} at {self.timestamp}"
