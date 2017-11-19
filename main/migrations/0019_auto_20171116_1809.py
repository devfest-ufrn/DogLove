# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-11-16 21:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0018_auto_20171116_1809'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pet',
            name='raca',
            field=models.CharField(choices=[(b'raca_desconhecida', b'Ra\xc3\xa7a Desconhecida'), (b'airedale_terrier', b'Airedale Terrier'), (b'boston_terrier', b'Boston Terrier'), (b'pastor-de-shetland', b'Pastor-de-Shetland'), (b'bichon_frise', b'Bichon Fris\xc3\xa9'), (b'norwich_terrier', b'Norwich Terrier'), (b'bulmastife', b'Bulmastife'), (b'bull_terrier', b'Bull Terrier'), (b'boiadeiro_de_berna', b'Boiadeiro de Berna'), (b'buldogue_frances', b'Buldogue Franc\xc3\xaas'), (b'bull_terrier', b'Bull Terrier'), (b'basset_hound', b'Basset Hound'), (b'corgi', b'Corgi'), (b'pequines', b'Pequin\xc3\xaas'), (b'malamute_do_alasca', b'Malamute do Alasca'), (b'lhasa_apso', b'Lhasa Apso'), (b'boiadeiro_australiano', b'Boiadeiro Australiano'), (b'terra_nova', b'Terra Nova'), (b'pointer_ingles', b'Pointer Ingl\xc3\xaas'), (b'saluki', b'Saluki'), (b'spitz_alemao', b'spitz_alemao'), (b'pastor_ingles', b'Pastor Ingl\xc3\xaas'), (b'affenpinscher', b'Affenpinscher'), (b'akita_inu', b'Akita_Inu'), (b'pastor_belga', b'Pastor Belga'), (b'cocker_spaniel', b'Cocker Spaniel'), (b'galgo_ingles', b'Galgo Ingl\xc3\xaas'), (b'maltes', b'Malt\xc3\xaas'), (b'pastor_australiano', b'Pastor Australiano'), (b'shih_tzu', b'Shih Tzu'), (b'yorkshite_terrier', b'Yorkshire Terrier'), (b'border_collie', b'Border Collie'), (b'chow_chow', b'Chow Chow'), (b'pit_bull', b'Pit Bull'), (b'pug', b'Pug'), (b'boxer', b'Boxer'), (b'chihuahua', b'Chihuahua'), (b'mastim_ingles', b'Mastim Ingl\xc3\xaas'), (b'husky_siberiano', b'Husky Siberiano'), (b'dachshund', b'Dachshund'), (b'dobermann', b'Dobermann'), (b'poodle', b'Poodle'), (b'dogue_alemao', b'Dogue Alem\xc3\xa3o'), (b'golden_retriever', b'Golden Retriever'), (b'buldogue', b'Buldogue'), (b'beagle', b'Beagle'), (b'rottweiler', b'Rottweiler'), (b'labrador_retriever', b'Labrador Retriever'), (b'pastor_alemao', b'Pastor Alem\xc3\xa3o')], default=b'raca_desconhecida', max_length=30),
        ),
    ]
