from django.conf.urls import url
from . import views

app_name = 'account'
urlpatterns = [
    #url(r'login', views.user_login, name='login'),
    url(r'^$', views.main, name='main'),
    url(r'^dashboard/$', views.dashboard, name='dashboard'),
]