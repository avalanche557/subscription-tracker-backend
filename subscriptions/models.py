from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User


class Subscription(models.Model):

    BILLING_CYCLE_CHOICES = [
        ('monthly', 'Monthly'),
        ('yearly', 'Yearly'),
        ('weekly', 'Weekly'),
    ]

    SOURCE_CHOICES = [
        ('manual', 'Manual'),
        ('sms', 'SMS'),
        ('email', 'Email'),
        ('bank', 'Bank Statement'),
    ]

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='subscriptions'
    )

    name = models.CharField(max_length=255)

    amount = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    billing_cycle = models.CharField(
        max_length=20,
        choices=BILLING_CYCLE_CHOICES,
        default='monthly'
    )

    next_billing_date = models.DateField()

    category = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )

    source = models.CharField(
        max_length=20,
        choices=SOURCE_CHOICES,
        default='manual'
    )

    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name