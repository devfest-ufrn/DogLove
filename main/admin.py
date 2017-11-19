from django.contrib import admin

from models import Profile
from models import Match, Mensagem, FaleConosco

admin.site.register(Match)
admin.site.register(Profile)
admin.site.register(FaleConosco)
