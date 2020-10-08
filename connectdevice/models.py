from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class ConnectDevice(models.Model):
    device_id = models.TextField()
    name = models.CharField(max_length=255)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class History(models.Model):
    device_id = models.ForeignKey(ConnectDevice, on_delete=models.CASCADE, related_name="deviceid")
    device_user_id = models.ForeignKey(ConnectDevice, on_delete=models.CASCADE, related_name="device_user_id")
    value = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
