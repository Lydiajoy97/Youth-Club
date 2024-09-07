from django.db import models
from django.conf import settings
import django.db.models.deletion
from django.contrib.auth.models import User
import datetime
import django


STATUS = ((0, "Draft"), (1, "Published"))


class ActivityForm(models.Model):
    first_name = models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='activity_form', to=settings.AUTH_USER_MODEL),
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

    def __str__(self):
        return f"ActivityForm {self.game_ideas} by {self.first_name}"