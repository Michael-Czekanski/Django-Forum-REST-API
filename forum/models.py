from django.db import models
from django.utils import timezone
from users.models import User

# Create your models here.

class Topic(models.Model):
    name = models.CharField(max_length=255)
    creation_date = models.DateTimeField(default=timezone.now)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.name} {self.created_by.username} {self.creation_date}"
