from rest_framework import viewsets
from ambulance.serializers.ambulanceSerializer import AmbulanceSerializer
from ambulance.models.ambulanceEntity import AmbulanceEntity

# Class that extends the ModelViewSet implementations of the operations CRUD(create, read, updete and delete) in the Data Base
class AmbulanceViewSet(viewsets.ModelViewSet):
    # Get all the registers of the table Ambulance in the data base
    queryset = AmbulanceEntity.objects.all()
    # Define the serializer class to be used with the objects recovered in with the "queryset" variable
    serializer_class = AmbulanceSerializer