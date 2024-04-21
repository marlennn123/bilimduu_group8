from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    age = models.PositiveSmallIntegerField(null=True, blank=True)
    country = models.CharField(max_length=30, null=True, blank=True)
    username = models.CharField(max_length=30, null=True, blank=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)


class Car(models.Model):
    category = models.CharField(max_length=30)
    marka = models.CharField(max_length=30)
    model = models.CharField(max_length=30)
    price = models.PositiveIntegerField()
    year = models.PositiveSmallIntegerField()
    mileage = models.PositiveIntegerField()
    city = models.CharField(max_length=30)
    country = models.CharField(max_length=30)
    with_photo = models.BooleanField(default=False)
    color = models.CharField(max_length=50)
    volume = models.FloatField()
    description = models.TextField()

    def __str__(self):
        return f"{self.marka} {self.model} ({self.year})"


class Bet(models.Model):
    number = models.IntegerField()
    total_number = models.IntegerField()
    buy_now = models.IntegerField()
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return f"Bet {self.number}"
