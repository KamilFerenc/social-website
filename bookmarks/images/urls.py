from django.conf.urls import url
from . import views


app_name = 'images'
urlpatterns = [
    url(r'^create/$', views.images_create, name='create'),
    url(r'^detail/(?P<id>\d+)/(?P<slug>[-\w]+)/$', views.detail_image,
        name='detail'),
    url(r'^like/$', views.image_like, name='like'),
    url(r'^$', views.image_list, name='list'),
    url(r'^ranking/$', views.image_ranking, name='image_ranking'),

]
