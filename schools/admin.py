from django.contrib import admin
from leaflet.admin import leafletGeoAdmin

from .models import School


class SchoolAdmin(leafletGeoAdmin):
    list_display = ['name', 'province', 'district', 'level', 'male', 'female']


admin.site.register(School, SchoolAdmin)
