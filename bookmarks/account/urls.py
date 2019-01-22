from django.conf.urls import url
from . import views
from django.urls import path
from django.contrib.auth import views as auth_views

app_name = 'account'
urlpatterns = [
    #url(r'login', views.user_login, name='login'),
    url(r'^$', views.main, name='main'),
    url(r'^dashboard/$', views.dashboard, name='dashboard'),
    url(r'^register/$', views.register, name='register'),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.activate, name='activate'),
    url(r'^edit/$', views.edit, name='edit'),
]
