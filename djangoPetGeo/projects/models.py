from django.db import models
from django.contrib.gis.db import models as geo_models


class Projects(models.Model):
    pass


class GeoObjects(models.Model):
    name = models.CharField(max_length=30)
    project = models.ForeignKey('Projects', on_delete=models.CASCADE)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class GeoPoint(GeoObjects):
    pass
