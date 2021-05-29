from django.urls import path
from . import views                    
urlpatterns = [
    path('', views.index),
    path('login', views.login),
    path('posting', views.posting),
    path('welcome/', views.welcome),
    path('register', views.reg),
    path('logout', views.logout),
    path('wall/<int:id>', views.commenting),
]