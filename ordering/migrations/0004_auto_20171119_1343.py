# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-19 20:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ordering', '0003_ordertable_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordertable',
            name='amount',
            field=models.IntegerField(max_length=200),
        ),
    ]