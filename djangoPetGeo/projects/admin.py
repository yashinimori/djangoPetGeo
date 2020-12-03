from django.contrib import admin
from .models import GeoPoint, Projects


class GeoPointAdmin(admin.ModelAdmin):
    list_display = ('name', 'geo_data')


admin.site.site_header = "Django Geo Pet"
admin.site.register(GeoPoint, GeoPointAdmin)
