"""Defines URL patterns for Ordering."""
from django.conf.urls import url
from . import views
urlpatterns = [
       # Home page

    url(r'^ordering/$', views.index, name='index'),
    url(r'^ordering/getToppings/(?P<pizza_id>[0-9]+)/$', views.getToppings, name='getToppings'),
    url(r'^ordering/saveView/$', views.saveView, name='saveView'),
   ]
