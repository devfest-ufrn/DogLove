# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-11-06 20:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_pet'),
    ]

    operations = [
        migrations.AddField(
            model_name='pet',
            name='idade',
            field=models.PositiveSmallIntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pet',
            name='situacao',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
    ]
