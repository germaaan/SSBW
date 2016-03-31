# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_restaurantes', '0003_restaurante_foto'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='restaurante',
            name='correo',
        ),
    ]
