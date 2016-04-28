from django.db import models
from django.template.defaultfilters import slugify

class Restaurante (models.Model):
	nombre = models.CharField(max_length=50, unique='True')
	direccion = models.CharField(max_length=100)
	foto = models.CharField(max_length=60, blank='True')
	votos = models.IntegerField(default=0)
	slug = models.SlugField(unique='True')

	def __unicode__(self):
		return self.nombre

	def save(self, *args, **kwargs):
		self.slug = slugify(self.nombre)
		super(Restaurante, self).save(*args, **kwargs)

class Plato (models.Model):
	restaurante = models.ForeignKey(Restaurante, on_delete=models.CASCADE)
	nombre = models.CharField(max_length=30)
	precio = models.DecimalField(max_digits=5, decimal_places=2)

	def save(self, *args, **kwargs):
		self.slug = slugify(self.nombre)
		super(Plato, self).save(*args, **kwargs)
