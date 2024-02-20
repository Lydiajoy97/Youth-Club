from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Form(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=254)
    consent = models.FileField()