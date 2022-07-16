from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    profile_picture = models.ImageField(upload_to='user_profile_pics', null=True, blank=True)
    bio = models.TextField(blank=True, default='No bio yet.')
    phone_number = models.CharField(max_length=20, default=0)
    gender = models.CharField(max_length=20, choices=[
        ('male', 'male'),
        ('female', 'female'),
        ('other', 'other')
    ], default=0)
    is_varified = models.BooleanField(default=False)