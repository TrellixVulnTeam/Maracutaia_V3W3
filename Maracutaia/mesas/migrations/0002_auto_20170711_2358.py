# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-12 03:58
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pedidos', '0002_auto_20170711_2358'),
        ('mesas', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comanda',
            name='item',
        ),
        migrations.AddField(
            model_name='comanda',
            name='pedido',
            field=models.ManyToManyField(to='pedidos.Item'),
        ),
        migrations.AlterField(
            model_name='comanda',
            name='data',
            field=models.DateTimeField(default=datetime.datetime(2017, 7, 11, 23, 58, 10, 936413)),
        ),
        migrations.AlterField(
            model_name='comanda',
            name='total',
            field=models.DecimalField(decimal_places=2, default='0,00', max_digits=5),
        ),
    ]
