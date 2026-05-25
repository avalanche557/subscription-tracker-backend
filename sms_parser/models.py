from django.db import models

# Create your models here.
from django.contrib.auth.models import User


class SMSMessage(models.Model):

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    sender = models.CharField(max_length=255)

    message = models.TextField()

    detected_merchant = models.CharField(
        max_length=255,
        blank=True,
        null=True
    )

    detected_amount = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        blank=True,
        null=True
    )

    is_subscription = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.sender