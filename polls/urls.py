'''
Created on 2018/10/18

@author: t16cs008
'''
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
]
