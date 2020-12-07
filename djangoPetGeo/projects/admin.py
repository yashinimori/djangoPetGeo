from django.contrib import admin
from leaflet.admin import LeafletGeoAdmin

from .models import Projects, GeoPoint, GeoLine, GeoPoly


class ProjectsAdmin(admin.ModelAdmin):
    fields = ('name',)


class GeoPointAdmin(LeafletGeoAdmin):
    list_display = ('name', 'geo_data')


class GeoLineAdmin(LeafletGeoAdmin):
    list_display = ('name', 'geo_data')


class GeoPolyAdmin(LeafletGeoAdmin):
    list_display = ('name', 'geo_data')


admin.site.site_header = "Django Geo Pet"
admin.site.register(Projects, ProjectsAdmin)
admin.site.register(GeoPoint, GeoPointAdmin)
admin.site.register(GeoLine, GeoLineAdmin)
admin.site.register(GeoPoly, GeoPolyAdmin)