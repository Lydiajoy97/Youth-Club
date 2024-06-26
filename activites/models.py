from django.db import models
from django.contrib.auth.models import User


STATUS = ((0, "Draft"), (1, "Published"))
class ActivityForm(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=254)
    game_ideas = models.CharField(max_length=700, blank=True)
    approved = models.BooleanField(default=False)
    status = models.IntegerField(choices=STATUS, default=0)