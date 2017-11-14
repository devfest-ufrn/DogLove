from django.contrib import admin

from models import Profile
from models import Match, Mensagem

admin.site.register(Match)
admin.site.register(Profile)
admin.site.register(Mensagem)

# Register your models here.
