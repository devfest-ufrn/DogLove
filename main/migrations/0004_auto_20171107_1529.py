# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-11-07 18:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20171106_1718'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pet',
            name='idade',
            field=models.PositiveSmallIntegerField(default=b'0'),
        ),
        migrations.AlterField(
            model_name='pet',
            name='situacao',
            field=models.BooleanField(default=b'true'),
        ),
    ]
