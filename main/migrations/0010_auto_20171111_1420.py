# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-11-11 17:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_auto_20171111_1358'),
    ]

    operations = [
        migrations.AlterField(
            model_name='match',
            name='user1status',
            field=models.CharField(choices=[(b'A', b'Aprovado'), (b'R', b'Rejeitado'), (b'N', b'NaoAvaliado')], default=b'N', max_length=1),
        ),
        migrations.AlterField(
            model_name='match',
            name='user2status',
            field=models.CharField(choices=[(b'A', b'Aprovado'), (b'R', b'Rejeitado'), (b'N', b'NaoAvaliado')], default=b'N', max_length=1),
        ),
        migrations.AlterUniqueTogether(
            name='match',
            unique_together=set([('user1', 'user2')]),
        ),
    ]
