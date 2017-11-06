from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include
from django.contrib.auth.views import logout
from main import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index, name='index'),
    url(r'^doglove/$', views.doglove, name='doglove'),
    url(r'^doglove/logout/$', logout, {'template_name': 'index.html', 'next_page': '/'}, name='sign-out'),
]
