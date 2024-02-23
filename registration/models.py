from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Form(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=254)
    age = models.CharField(max_length=20, default=10)
    group_attending = models.CharField(max_length=200, default="The Hub")
    photo_consent = models.BooleanField(default=True)
    addional_information = models.CharField(max_length=700, blank=True)
    trip_consent_letter = models.FileField(blank=True)