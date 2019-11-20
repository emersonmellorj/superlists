# URLs da aplicacao lists

from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home_page, name='home'),
    path('java_script/', views.java_script, name='java_script'),
]