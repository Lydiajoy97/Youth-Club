from django.db import models
from django.contrib.auth.models import User


STATUS = ((0, "Draft"), (1, "Published"))
# checkbox field source in credits
# Create your models here.
class form(models.Model):
    first_name = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="form_upload")
    last_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=254)
    age = models.CharField(max_length=20, default=10)
    group_attending = models.CharField(max_length=200, default="The Hub")
    photo_consent = models.BooleanField(default=True)
    addional_information = models.CharField(max_length=700, blank=True)
    consent_letter = models.FileField(blank=True)
    status = models.IntegerField(choices=STATUS, default=0)

    def __str__(self):
        return self.first_name