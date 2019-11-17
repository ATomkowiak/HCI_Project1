from django.conf.urls import url
from django.contrib import admin
from django.urls import path

from uploads.core import views


urlpatterns = [
    url('^$', views.glowna, name='home'),
    url('data_analysis/', views.data_analysis, name='data_analysis'),
    url('about/', views.about, name='about'),
    url('contact/', views.contact, name='contact'),
    url('lekcje/podstawy/', views.podstawy, name='podstawy'),
    url('lekcje/instrukcje_warunkowe/', views.ins_warun, name='ins_warun'),
    url('lekcje/petle/', views.petle, name='petle'),
    url('lekcje/liczby_pseudolosowe/', views.pseudolos, name='pseudolos'),
    url('lekcje/listy/', views.listy, name='listy'),
    url('lekcje/slowniki/', views.slowniki, name='slowniki'),
    url('lekcje/lancuchy_znakow/', views.lancuch, name='lancuch'),
    url('lekcje/funkcje/', views.funkcje, name='funkcje'),
    url('lekcje/klasy/', views.klasy, name='klasy'),



]
