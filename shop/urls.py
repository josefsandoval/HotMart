from django.contrib.auth.urls import url
from . import views
from django.contrib.auth.views import login, logout

urlpatterns = [
    url(r'^$', views.index),
    url(r'^login/$', login, {'template_name': 'shop/login.html'}),
    url(r'^logout/$', logout, {'template_name': 'shop/login.html'}),
    url(r'^register/$', views.register, name='register')
]

