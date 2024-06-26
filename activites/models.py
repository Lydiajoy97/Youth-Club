from django.db import models
from django.contrib.auth.models import User


STATUS = ((0, "Draft"), (1, "Published"))
# checkbox field source in credits
# Create your models here.
class ActivityForm(models.Model):
    name = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="activity_form")
    email = models.EmailField(max_length=254)
    game_ideas = models.CharField(max_length=700, blank=True)
    approved = models.BooleanField(default=False)
    status = models.IntegerField(choices=STATUS, default=0)

    def __str__(self):
        return self.first_name