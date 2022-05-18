from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('main/', views.main),
    path("ajout/<int:id>/", views.ajout),
    path("ajoutdisquaire/", views.ajoutdisquaire),
    path("traitement/<int:id>/", views.traitement),
    path("traitementdisquaire", views.traitementdisquaire),
    path("alldisquaire/", views.alldisquaire),
    path('affichedisquaire/<int:id>/', views.affichedisquaire),
    path('updatedisquaire/<int:id>/', views.updatedisquaire),
    path('traitementupdatedisquaire/<int:id>', views.traitementupdatedisquaire),
    path('update/<int:id>/', views.update),
    path('traitementupdate/<int:id>', views.traitementupdate),
    path('delete/<int:id>/', views.delete),
    path('deletedisquaire/<int:id>/', views.deletedisquaire),
    path('affichedisque/<int:id>/', views.affichedisque),
]