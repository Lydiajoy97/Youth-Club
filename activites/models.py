from django.db import models
from django.conf import settings
import django.db.models.deletion
from django.contrib.auth.models import User
import datetime
import django


STATUS = ((0, "Draft"), (1, "Published"))


class ActivityForm(models.Model):
    email = models.EmailField(max_length=254)
    game_ideas = models.TextField()
    approved_by = models.BooleanField(default=False)
    status = models.IntegerField(choices=STATUS, default=0)
    updated_on = models.DateTimeField(default=datetime.datetime.now)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="addactivity", default=0,
    )
    
    class Meta:
        ordering = ["updated_on"]