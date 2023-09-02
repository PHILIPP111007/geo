from django.contrib import admin
from .models import IPv4Location, IPv6Location


@admin.register(IPv4Location)
class IPv4LocationAdmin(admin.ModelAdmin):
    pass

@admin.register(IPv6Location)
class IPv6LocationAdmin(admin.ModelAdmin):
    pass
