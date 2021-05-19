from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('destroy/', views.destroy),
    path('addtwo/', views.addtwo),
    path('inp', views.inp),

]
