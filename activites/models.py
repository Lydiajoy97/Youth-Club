from django.db import models
from django.contrib.auth.models import User


STATUS = ((0, "Draft"), (1, "Published"))
class ActivityForm(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=254)
    game_ideas = models.TextField()
    approved = models.BooleanField(default=False)
    status = models.IntegerField(choices=STATUS, default=0)
    created_on = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"ActivityForm {self.game_ideas} by {self.name}"