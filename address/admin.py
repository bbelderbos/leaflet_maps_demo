from django.contrib import admin
from .models import Address


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ("address", "lat", "lon", "created")
    search_fields = ("address",)
    list_filter = ("created",)
