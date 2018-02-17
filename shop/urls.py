from django.conf.urls import include
from django.contrib.auth.urls import url
from . import views
from django.contrib.auth.views import login, logout

urlpatterns = [
    url(r'^$', views.index),
    url(r'^login/$', login, {'template_name': 'shop/login.html'}, name = 'login'),
    url(r'^logout/$', logout, {'template_name': 'shop/home.html'}),
    url(r'^register/$', views.register, name='register'),
    url(r'^auth/', include('social_django.urls', namespace='social')),  # <- for social Authentication
]

