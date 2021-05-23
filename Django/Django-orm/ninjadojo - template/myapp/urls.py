from django.urls import path
from . import views                    
urlpatterns = [
    path('', views.index),
    path('data1', views.dojojo),
    path('data2', views.ninjaja),
]