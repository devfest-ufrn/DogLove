# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-11-16 20:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0016_mensagem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pet',
            name='raca',
            field=models.CharField(choices=[(b'raca_desconhecida', b'Ra\xc3\xa7a Desconhecida'), (b'airedale_terrier', b'Airedale Terrier'), (b'boston_terrier', b'Boston Terrier'), (b'pastor-de-shetland', b'Pastor-de-Shetland'), (b'bichon_frise', b'Bichon Fris\xc3\xa9'), (b'norwich_terrier', b'Norwich Terrier'), (b'bulmastife', b'Bulmastife'), (b'bull_terrier', b'Bull Terrier'), (b'boiadeiro_de_berna', b'Boiadeiro de Berna'), (b'buldogue_frances', b'Buldogue Franc\xc3\xaas'), (b'bull_terrier', b'Bull Terrier'), (b'basset_hound', b'Basset Hound')], default=b'raca_desconhecida', max_length=30),
        ),
    ]
