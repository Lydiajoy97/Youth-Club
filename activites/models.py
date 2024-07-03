from django.db import models
from django.contrib.auth.models import User


STATUS = ((0, "Draft"), (1, "Published"))


class ActivityForm(models.Model):
    first_name = models.CharField(max_length=200, default="id")
    email = models.EmailField(max_length=254)
    game_ideas = models.TextField()
    approved_by = models.BooleanField(default=False)
    status = models.IntegerField(choices=STATUS, default=0)
    updated_on = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="addactivity"
    )
    
    class Meta:
        ordering = ["updated_on"]

    def __str__(self):
        return f"ActivityForm {self.game_ideas} by {self.first_name}"