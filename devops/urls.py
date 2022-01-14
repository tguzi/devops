# from django.conf.urls import re_path
from django.urls.conf import path
from . import views

urlpatterns = [
    path('index/', views.index)
    # re_path(r'^index/$', views.index, name='index')
    # re_path(r'^$', views.hello)
]