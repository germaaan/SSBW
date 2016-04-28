# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_restaurantes', '0004_remove_restaurante_correo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurante',
            name='foto',
            field=models.CharField(max_length=60, blank=b'True'),
        ),
        migrations.AlterField(
            model_name='restaurante',
            name='nombre',
            field=models.CharField(unique=b'True', max_length=50),
        ),
        migrations.AlterField(
            model_name='restaurante',
            name='slug',
            field=models.SlugField(unique=b'True'),
        ),
    ]
