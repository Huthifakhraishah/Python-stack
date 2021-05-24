from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('authors/', views.index2),
    path('books',views.add),
    path ('author',views.add2),
    path ('books/<int:id>',views.view),
    path ('addauther',views.adduth),
    path ('authors/authors/<int:id>',views.view2),
    path ('addbook',views.addbook)

]