from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from accounts.models import account


class OTP(models.Model):
    email = models.EmailField(unique=True)
    token = models.CharField(max_length=6)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.otp_code
    