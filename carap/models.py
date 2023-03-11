from django.db import models

# Create your models here.
class categoria(models.Model):
    vehiculo=models.CharField(max_length= 400)
    modelo=models.ImageField()
class conductor(models.Model):
    nombre=models.CharField(max_length=30)
    apellido=models.CharField(max_length=30)
    email=models.EmailField()
class equipo(models.Model):
    nombre=models.CharField(max_length=40)
    marca=models.CharField(max_length=30)
class ganadores(models.Model):
    nombre=models.CharField(max_length=30)
    fechalimite=models.DateTimeField()
    fechadellegada=models.BooleanField()