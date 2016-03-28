from django.db import models
from django.template.defaultfilters import slugify

class Restaurante (models.Model):
	nombre    = models.CharField(max_length=30)
	direccion = models.CharField(max_length=60)
	email     = models.EmailField()
    slug      = models.SlugField()

    def save(self, *args, **kwargs):
		self.slug = slugify(self.nombre)
		super(Restaurante, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.nombre

class Plato (models.Model):
	restaurante = models.ForeingKey(Restaurante, on_delete=models.CASCADE)
	nombre      = models.CharField(max_lenght=30)
	precio      = models.DecimalField(max_digits=3, decimal_places=1)
	foto        = models.ImageField(upload_to='profile_images', blank=True)

    def save(self, *args, **kwargs):
		self.slug = slugify(self.nombre)
		super(Plato, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.nombre

    def barato(self):
		if self.precio < 10:
			return "barato"
		else:
			return "caro"
