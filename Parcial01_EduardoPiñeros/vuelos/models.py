from django.db import models
tipos_de_vuelo = [
 ('Nacional','Nacional'),
 ('Internacional','Internacional')   
]

# Create your models here.
class Flight(models.Model):
    name = models.CharField(max_length=255)
    tipo = models.CharField(max_length=255, choices=tipos_de_vuelo)
    price = models.FloatField()