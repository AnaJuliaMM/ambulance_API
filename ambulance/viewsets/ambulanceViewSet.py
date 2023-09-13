
# Import necessary modules from the Django Rest Framework
from rest_framework import viewsets

# Import the serializer and model for the AmbulanceEntity
from ambulance.serializers.ambulanceSerializer import AmbulanceSerializer
from ambulance.models.ambulanceEntity import AmbulanceEntity

class AmbulanceViewSet(viewsets.ModelViewSet):
    """
    A viewset class for managing AmbulanceEntity instances.

    Attributes:
        queryset (QuerySet): A queryset to retrieve all AmbulanceEntity objects from the database.
        serializer_class (Serializer): The serializer class for serializing and deserializing AmbulanceEntity objects.
    """

    # Set the queryset to retrieve all AmbulanceEntity objects from the database
    queryset = AmbulanceEntity.objects.all()

    # Set the serializer class to use for serializing and deserializing AmbulanceEntity objects
    serializer_class = AmbulanceSerializer
