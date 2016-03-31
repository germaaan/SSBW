from django.db import models
from django.template.defaultfilters import slugify

class Restaurante (models.Model):
	slug = models.SlugField(unique=True)
	nombre = models.CharField(max_length=50, unique=True)
	direccion = models.CharField(max_length=100)
	correo = models.CharField(max_length=100)
	votos = models.IntegerField(default=0)

	def __unicode__(self):
		return self.nombre

	def save(self, *args, **kwargs):
		self.slug = slugify(self.nombre)
		super(Restaurante, self).save(*args, **kwargs)

class Plato (models.Model):
	restaurante = models.ForeignKey(Restaurante, on_delete=models.CASCADE)
	nombre = models.CharField(max_length=30)
	precio = models.DecimalField(max_digits=5, decimal_places=2)

	def __unicode__(self):
		return self.nombre
