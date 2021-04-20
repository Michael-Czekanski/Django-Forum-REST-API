from django.db import models
from django.contrib.auth import AbstractUser

# Create your models here.

class User(AbstractUser):
    """Custom User class."""

    email = models.EmailField(unique=True)
