# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-19 19:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizzas', '0004_pizza_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pizza',
            name='price',
            field=models.IntegerField(max_length=200),
        ),
    ]
