from django.contrib import admin
from django.urls import path, include

#Importando os ViewSets
""" Teste: utilizando ViewSets sem o DefaultRoute()"""
from .viewsets.ambulanceViewSet import AmbulanceViewSet
from .viewsets.paramedicViewSet import ParamedicViewSet

#Importando os View
""" Teste: View Baseado em Funções"""



urlpatterns = [
    path('ambulances/', AmbulanceViewSet.as_view({'get': 'list'})),
    path('ambulances/cadastrar/',  AmbulanceViewSet.as_view({'post': 'create'})),
    path('paramedics/', ParamedicViewSet.as_view({'get': 'list'})), #redireciona para o arquivo urls.py da aplicação "ambulancw"
    path('paramedics/cadastrar',  ParamedicViewSet.as_view({'post': 'create'})),
]

