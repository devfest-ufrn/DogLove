# -*- coding: utf-8 -*-

import datetime
import uuid
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from location_field.models.plain import PlainLocationField
from django.utils.encoding import python_2_unicode_compatible
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    ddd = models.CharField(max_length=2, default='00')
    celular = models.CharField(max_length=9, default='000000000')
    rua = models.CharField(max_length=255, help_text='Digite seu endereço e confira o local no mapa')
    endereco = PlainLocationField(based_fields=['rua'], zoom=7)
    qntComb = models.IntegerField(default='0')
    cadastrouPet = models.BooleanField(default=False)
    def __str__(self):
        return self.user.username
    
def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'user_{0}/{1}'.format(instance.user.id,filename)

class Pet (models.Model):
    
    PORTE_ESCOLHAS = (
        ('pequeno', 'Pequeno'),
        ('medio', 'Medio'),
        ('grande', 'Grande'),
    )
    
    SEXO_ESCOLHAS = (
        ('F', 'Fêmea'),
        ('M', 'Macho'),
    )
    
    RACA_ESCOLHAS = (
        ('raca_desconhecida', 'Raça Desconhecida'),
        ('airedale_terrier', 'Airedale Terrier'),
        ('boston_terrier', 'Boston Terrier'),
        ('pastor_de_shetland', 'Pastor de Shetland'),
        ('bichon_frise', 'Bichon Frisé'),
        ('norwich_terrier', 'Norwich Terrier'),
        ('bulmastife', 'Bulmastife'),
        ('bull_terrier', 'Bull Terrier'),
        ('boiadeiro_de_berna', 'Boiadeiro de Berna'),
        ('buldogue_frances', 'Buldogue Francês'),
        ('bull_terrier', 'Bull Terrier'),
        ('basset_hound', 'Basset Hound'),
        ('corgi', 'Corgi'),
        ('pequines', 'Pequinês'),
        ('malamute_do_alasca', 'Malamute do Alasca'),
        ('lhasa_apso', 'Lhasa Apso'),
        ('boiadeiro_australiano', 'Boiadeiro Australiano'),
        ('terra_nova', 'Terra Nova'),
        ('pointer_ingles', 'Pointer Inglês'),
        ('saluki', 'Saluki'),
        ('spitz_alemao', 'Spitz Alemão'),
        ('pastor_ingles', 'Pastor Inglês'),
        ('affenpinscher', 'Affenpinscher'),
        ('akita_inu', 'Akita Inu'),
        ('pastor_belga', 'Pastor Belga'),
        ('cocker_spaniel', 'Cocker Spaniel'),
        ('galgo_ingles', 'Galgo Inglês'),
        ('maltes', 'Maltês'),
        ('pastor_australiano', 'Pastor Australiano'),
        ('shih_tzu', 'Shih Tzu'),
        ('yorkshire_terrier', 'Yorkshire Terrier'),
        ('border_collie', 'Border Collie'),
        ('chow_chow', 'Chow Chow'),
        ('pit_bull', 'Pit Bull'),
        ('pug', 'Pug'),
        ('boxer', 'Boxer'),
        ('chihuahua', 'Chihuahua'),
        ('mastim_ingles', 'Mastim Inglês'),
        ('husky_siberiano', 'Husky Siberiano'),
        ('dachshund', 'Dachshund'),
        ('dobermann', 'Dobermann'),
        ('poodle', 'Poodle'),
        ('dogue_alemao', 'Dogue Alemão'),
        ('golden_retriever', 'Golden Retriever'),
        ('buldogue', 'Buldogue'),
        ('beagle', 'Beagle'),
        ('rottweiler', 'Rottweiler'),
        ('labrador_retriever', 'Labrador Retriever'),
        ('pastor_alemao', 'Pastor Alemão'),
        ('sao_bernardo', 'São Bernardo'),
        ('shiba_inu', 'Shiba Inu'),
    )
    
    RACA_ESCOLHAS2 = sorted(RACA_ESCOLHAS)
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    porte = models.CharField(max_length=8,choices=PORTE_ESCOLHAS, default='pequeno')
    nome = models.CharField(max_length=15, default='nome')
    raca = models.CharField(max_length=30, default='raca_desconhecida', choices=RACA_ESCOLHAS2)
    idade = models.PositiveSmallIntegerField(default='0')
    sexo = models.CharField(max_length=1, choices=SEXO_ESCOLHAS, default='Macho')
    situacao = models.BooleanField(default='true')
    foto = models.ImageField(upload_to=user_directory_path, default=settings.MEDIA_ROOT + 'padrao.jpg')
    bio = models.TextField(max_length=500, default='bio')
    
    def __str__(self):
        return self.user.username
    
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def create_user_pet(sender, instance, created, **kwargs):
    if created:
        Pet.objects.create(user=instance)
        
@receiver(post_save, sender=User)
def save_user_pet(sender, instance, **kwargs):
    instance.pet.save()

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
    
class Match (models.Model):
    
    STATUS_ESCOLHAS = (
        ('A', 'Aprovado'),
        ('R', 'Rejeitado'),
        ('N', 'NaoAvaliado'),
    )
    
    user1 = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user1")
    user2 = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user2")
    user1status = models.CharField(max_length=1, choices=STATUS_ESCOLHAS, default='N')
    user2status = models.CharField(max_length=1, choices=STATUS_ESCOLHAS, default='N')
    data = models.DateTimeField(auto_now_add=True)
    distancia = models.FloatField(default='999999999')
    
    def __str__(self):           
        return str(self.id)
    
    class Meta:
        ordering = ('data',)
        unique_together = (("user1", "user2"),)
        
class Mensagem (models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    conteudo = models.CharField(max_length=300)
    sender = models.CharField(max_length=150)
    match = models.ForeignKey(Match, on_delete=models.CASCADE, related_name="mensagens")
    
    class Meta:
        ordering = ('timestamp',)
