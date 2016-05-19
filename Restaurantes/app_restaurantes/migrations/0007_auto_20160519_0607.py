# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_restaurantes', '0006_auto_20160519_0605'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plato',
            name='nombre',
            field=models.CharField(max_length=30),
        ),
    ]
