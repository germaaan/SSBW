# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Plato',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=30)),
                ('precio', models.DecimalField(max_digits=5, decimal_places=2)),
            ],
        ),
        migrations.CreateModel(
            name='Restaurante',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('slug', models.SlugField(unique=True)),
                ('nombre', models.CharField(unique=True, max_length=50)),
                ('direccion', models.CharField(max_length=100)),
                ('correo', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='plato',
            name='restaurante',
            field=models.ForeignKey(to='app_restaurantes.Restaurante'),
        ),
    ]
