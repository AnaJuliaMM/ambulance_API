from rest_framework import viewsets
from ambulance.serializers.ambulanceSerializer import AmbulanceSerializer
from ambulance.models.ambulanceEntity import AmbulanceEntity

class AmbulanceViewSet(viewsets.ModelViewSet):
    queryset = AmbulanceEntity.objects.all()
    serializer_class = AmbulanceSerializer