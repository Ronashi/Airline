from django.contrib import admin

from .model import Flight, Airport
# Register your models here.
admin.site.register(Airport)
admin.site.register(Flight, FlightAdmin)
