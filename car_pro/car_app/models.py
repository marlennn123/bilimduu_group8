from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models


class CustomUser(AbstractUser):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(unique=True)
    groups = models.ManyToManyField(Group, verbose_name=('groups'), blank=True, related_name='customuser_groups')
    user_permissions = models.ManyToManyField(Permission, verbose_name=('user permissions'), blank=True,
                                              related_name='customuser_user_permissions')

    def __str__(self):
        return self.email


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
