from django.db import models

# From https://reintech.io/blog/building-a-messaging-system-in-django
# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=100)

class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name="sent_messages")
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name="received_messages")
    subject = models.CharField(max_length=200)
    body = models.TextField()
    email = models.TextField()