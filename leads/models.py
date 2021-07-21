from django.db import models
from .constants import LEAD_STATUS, FRESH
from accounts.models import User


class Lead(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=False)
    course = models.TextField(null=True, blank=True)
    interest = models.TextField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    status = models.CharField(max_length=50, choices=LEAD_STATUS, default=FRESH)
    claim_by = models.ForeignKey(User, related_name='lead_claim_by', null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.email
