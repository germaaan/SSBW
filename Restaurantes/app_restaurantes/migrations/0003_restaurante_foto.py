# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_restaurantes', '0002_restaurante_votos'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurante',
            name='foto',
            field=models.CharField(max_length=60, blank=True),
        ),
    ]
