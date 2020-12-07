from django.contrib.gis.db import models as geo_models
from django.db import models


class Projects(models.Model):
    name = models.CharField(max_length=30)


class GeoObjects(geo_models.Model):
    name = models.CharField(max_length=30)
    project = models.ForeignKey('Projects', on_delete=models.CASCADE)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class GeoPoint(GeoObjects):
    geo_data = geo_models.PointField()


class GeoLine(GeoObjects):
    geo_data = geo_models.LineStringField()


class GeoPoly(GeoObjects):
    geo_data = geo_models.PolygonField()
