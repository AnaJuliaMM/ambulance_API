"""
URL configuration for the core project.

The `urlpatterns` list routes URLs to views. For more information, please see:
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

# Import necessary modules from Django
from django.contrib import admin
from django.urls import path, include

# Import modules for API views and documentation
from rest_framework import routers
from ambulance.viewsets.ambulanceViewSet import AmbulanceViewSet
from ambulance.viewsets.paramedicViewSet import ParamedicViewSet
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

# Define the schema view for API documentation
schema_view = get_schema_view(
    openapi.Info(
        title="core API",
        default_version='v1',
        description="API documentation for the core project",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@core.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

# Create a router for defining API routes and views
route = routers.DefaultRouter()
route.register('ambulances', AmbulanceViewSet)
route.register('paramedics', ParamedicViewSet)

# Define the URL patterns for the project
urlpatterns = [
    path('admin/', admin.site.urls),
    # Redirects to the 'urls.py' file of the 'ambulance' application
    path('', include(route.urls)),
]

# Include Swagger and ReDoc documentation URLs
urlpatterns += [
   path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
