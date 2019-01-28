from django.conf.urls import url
from . import views


app_name = 'images'
urlpatterns = [
    url(r'^create/$', views.images_create, name='create'),
    url(r'^detail/(?P<id>\d+)/(?P<slug>[-\w]+)/$', views.detail_image,
        name='detail'),

]
