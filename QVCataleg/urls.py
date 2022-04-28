from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.principal_view, name='principal'),
    # Per mostrar el mapa
    path('mostraMapa/<int:mapa>/<int:tip>', views.mostraMapa),
    path('mostraMapaCompost/<int:mapa>', views.mostraMapaCompost),
    path('usuaris/', include('django.contrib.auth.urls')),
    path('catalegDinamic/', views.catalegDinamic_view, name='catalegDinamic'),
    path('catalegDinamicCapes/', views.catalegDinamicCapes_view, name='catalegDinamicCapes'),
    path('pokemon/', views.pokemon_view, name='pokemon'),
    path('test/', views.test_view, name='test'),
    path('nouMapa/<str:tipus>/', views.mapaForm_view, name='nouMapa'),
    path('editaMapa/<int:mapa>/', views.editaMapaForm_view, name='editaMapa'),
    path('esborraMapa/<int:mapa>/', views.esborraMapaForm_view, name='esborraMapa'),
    path('esborraMapaCompost/<int:mapa>/', views.esborraMapaCompostForm_view, name='esborraMapaCompost'),

]
