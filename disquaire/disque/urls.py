from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('index/', views.index),
    path('main/', views.main),
    path("ajout/", views.ajout),
    path("ajoutdisquaire/", views.ajoutdisquaire),
    path("traitement", views.traitement),
    path("traitementdisquaire", views.traitementdisquaire),
    path("all/", views.all),
    path("alldisquaire/", views.alldisquaire),
    path('affichedisquaire/<int:id>/', views.affichedisquaire),
    path('updatedisquaire/<int:id>/', views.updatedisquaire),
    path('traitementupdatedisquaire/<int:id>', views.traitementupdatedisquaire),
    path('affiche/<int:id>/', views.affiche),
    path('update/<int:id>/', views.update),
    path('traitementupdate/<int:id>', views.traitementupdate),
    path('delete/<int:id>/', views.delete),
    path('deletedisquaire/<int:id>/', views.deletedisquaire),
    path('test/', views.test),
]