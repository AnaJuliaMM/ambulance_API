# Import necessary modules from the Django Rest Framework
from rest_framework import viewsets

# Import the serializer and model for the ParamedicEntity
from ambulance.serializers.paramedicSerializer import ParamedicSerializer
from ambulance.models.paramedicEntity import ParamedicEntity

class ParamedicViewSet(viewsets.ModelViewSet):
    """
    A viewset class for handling ParamedicEntity instances.

    Attributes:
        queryset (QuerySet): A queryset to retrieve all ParamedicEntity objects from the database.
        serializer_class (Serializer): The serializer class for serializing and deserializing ParamedicEntity objects.
    """

    # Set the queryset to retrieve all ParamedicEntity objects from the database
    queryset = ParamedicEntity.objects.all()

    # Set the serializer class to use for serializing and deserializing ParamedicEntity objects
    serializer_class = ParamedicSerializer
