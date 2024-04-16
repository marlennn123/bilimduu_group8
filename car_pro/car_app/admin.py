from django.contrib import admin
from .models import Car, Bet


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ['category', 'marka', 'model', 'price', 'year', 'city']
    list_filter = ['category', 'marka', 'model', 'year', 'city']
    search_fields = ['marka', 'model', 'city', 'country']


@admin.register(Bet)
class BetAdmin(admin.ModelAdmin):
    list_display = ['number', 'total_number', 'start_date', 'end_date']
    list_filter = ['start_date', 'end_date']
    search_fields = ['number']

