from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    phone = models.CharField(max_length=11, unique=True)
    address = models.TextField(blank=True, null=True)
    is_customer = models.BooleanField(default=True)
    is_staff_member = models.BooleanField(default=False)

    def __str__(self):
        return self.username
