from rest_framework import viewsets
from ambulance.serializers.paramedicSerializer import ParamedicSerializer
from ambulance.models.paramedicEntity import ParamedicEntity

class ParamedicViewSet(viewsets.ModelViewSet):
    queryset = ParamedicEntity.objects.all()
    serializer_class = ParamedicSerializer