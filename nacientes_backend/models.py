from django.db import models
from django.contrib.gis.db import models

# Create your models here.
class Naciente(models.Model):
    wkt = models.CharField(max_length=254, null=True)
    sistema_de = models.CharField(max_length=254, null=True)
    punto_de_m = models.CharField(max_length=254, null=True)
    n = models.CharField(max_length=254, null=True)
    e = models.CharField(max_length=254, null=True)
    nitrato = models.CharField(max_length=254, null=True)
    distrito = models.CharField(max_length=254, null=True)
    canton = models.CharField(max_length=254, null=True)
    provincia = models.CharField(max_length=254, null=True)
    r_cont_n = models.CharField(max_length=254, null=True)
    c_canton = models.CharField(max_length=254, null=True)
    point_x = models.CharField(max_length=254, null=True)
    point_y = models.CharField(max_length=254, null=True)
    id_n = models.IntegerField(null=True)
    c_distrito = models.IntegerField(null=True)
    geom = models.PointField()

    def __int__(self): return self.id_n