from rest_framework import viewsets
from ambulance.serializers.paramedicSerializer import ParamedicSerializer
from ambulance.models.paramedicEntity import ParamedicEntity

# Class that extends the ModelViewSet implementations of the operations CRUD(create, read, updete and delete) in the Data Base
class ParamedicViewSet(viewsets.ModelViewSet):
    #Get all the registers of the table Paramedic in the data base
    queryset = ParamedicEntity.objects.all()
    # Define the serializer class to be used with the objects recovered in with the "queryset" variable
    serializer_class = ParamedicSerializer