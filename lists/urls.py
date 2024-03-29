# URLs da aplicacao lists

from django.contrib import admin
from django.urls import path, include, re_path
from . import views

urlpatterns = [
    path('', views.home_page, name='home'),
    re_path(r'^(\d+)/$', views.view_list, name='view_list'),
    re_path(r'^new$', views.new_list, name='new_list'),
    #re_path(r'^(\d+)/add_item$', views.add_item, name='add_item'),
]