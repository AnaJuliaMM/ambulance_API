# Import necessary modules from the Django Rest Framework
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from rest_framework.exceptions import ValidationError  # Import exception 'ValidationError'


# Import the serializer and model for the ParamedicEntity
from ambulance.serializers.paramedicSerializer import ParamedicSerializer
from ambulance.models.paramedicEntity import ParamedicEntity
from ambulance.models.ambulanceEntity import AmbulanceEntity

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



    def get_object(self, data, key):
        """
        A method that retrieves a value based on its key and found an object whose pk is equal to the value retrieved
    
        Args:
            data (dict): receives the data  of a request
            key (str): the key whose value contains the object pk

        Raises:
            Http404: an exception raises in case the key was not found

        Returns:
            AmbulanceEntity: returns an object whose pk is the one found in the data
        """
        try:
            return  AmbulanceEntity.objects.get(pk = data.get(key))
        except:
            raise Http404


    def create(self, request, *args, **kwargs):
        """
        Create a new paramedic object in the database receving the table attributes values

        Arguments:
            request (POST): receives a request with JSON data
        Returns:
            Dict: returns a structure with "message" key that prints a messsage of sucess and "data" key with the new object created
        """
        try:
            ambulance = self.get_value(request.data, "ambulance")
            serializer = ParamedicSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save(ambulance=ambulance)
            return Response({'message': 'Objeto criado com sucesso', 'data': serializer.data})
        except ValidationError as e:
            return Response({'message': 'Erro de validação', 'errors': e.detail}, status=status.HTTP_400_BAD_REQUEST)


        # Personalize a resposta de acordo com suas necessidades
        return Response({'message': 'Objeto criado com sucesso', 'data': serializer.data})





