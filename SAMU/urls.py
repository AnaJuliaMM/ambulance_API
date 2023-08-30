"""
URL configuration for SAMU project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include



"""
Para projetos grande: utilizar o classe DefaultRouter() Roteador Padrão

from rest_framework import routers
from ambulance.viewsets.ambulanceViewSet import AmbulanceViewSet
from ambulance.viewsets.paramedicViewSet import ParamedicViewSet

route = routers.DefaultRouter()
route.register('ambulance', AmbulanceViewSet)
route.register('paramedic', ParamedicViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(route.urls)),
]

"""

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ambulances/', include('ambulance.urls')), #redireciona para o arquivo urls.py da aplicação "ambulancw"
]
