from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include
from django.contrib.auth.views import logout
from main import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index, name='index'),
    url(r'^doglove/$', views.principal, name='principal'),
    url(r'^doglove/buscar$', views.principal, name='buscar'),
    url(r'^doglove/logout$', logout, {'template_name': 'index.html', 'next_page': '/'}, name='sign-out'),
    url(r'^doglove/meupet$', views.meupet, name='meupet'),
    url(r'^doglove/definirendereco$', views.definirEndereco, name='definirEndereco'),
    url(r'^doglove/cadastrarPet$', views.cadastrarPet, name='cadastrarPet'),
    url(r'^doglove/minhascombinacoes$', views.minhasCombinacoes, name='minhasCombinacoes'),
    url(r'^doglove/minhascombinacoes/(?P<destinatario>.+)$', views.enviarMensagem, name='enviarMensagem'),
    url(r'^doglove/cancelar/(?P<usuario>.+)$', views.cancelarMatch, name='cancelarMatch'),
    url(r'^doglove/configuracoes$', views.configuracoes, name='configuracoes'),
    url(r'^doglove/filtros$', views.filtros, name='filtros'),
    url(r'^doglove/aceitar/(?P<usuarioAceito>.+)$', views.aceitar, name='aceitar'),
    url(r'^doglove/rejeitar/(?P<usuarioAceito>.+)$', views.rejeitar, name='rejeitar'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
