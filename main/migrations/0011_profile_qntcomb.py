# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-11-12 18:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_auto_20171111_1420'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='qntComb',
            field=models.IntegerField(default=b'0'),
        ),
    ]
