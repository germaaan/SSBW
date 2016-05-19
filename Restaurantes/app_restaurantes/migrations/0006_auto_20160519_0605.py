# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_restaurantes', '0005_auto_20160428_1525'),
    ]

    operations = [
        migrations.AddField(
            model_name='plato',
            name='slug',
            field=models.SlugField(default=''),
        ),
        migrations.AlterField(
            model_name='plato',
            name='nombre',
            field=models.CharField(unique='True', max_length=30),
        ),
    ]
