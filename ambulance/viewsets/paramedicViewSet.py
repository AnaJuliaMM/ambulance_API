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



    def get_ambulance(self, pk):
        """
        Retrieve an AmbulanceEntity object by its primary key.

        Args:
            pk (int): The primary key of the AmbulanceEntity to retrieve.

        Raises:
            Http404: Raised when no AmbulanceEntity with the specified primary key is found.

        Returns:
            AmbulanceEntity: An AmbulanceEntity object with the specified primary key.
        """
        try:
            return AmbulanceEntity.objects.get(pk=pk)
        except AmbulanceEntity.DoesNotExist:
            raise Http404("Ambulance not found")



    def create(self, request, *args, **kwargs):
        """
        Create a new paramedic object in the database receving the table attributes values

        Arguments:
            request (POST): receives a request with JSON data
        Returns:
            Dict: returns a structure with "message" key that prints a messsage of sucess and "data" key with the new object created
        """
        try:
            ambulance = self.get_ambulance(request.data.get("ambulance"))
            serializer = ParamedicSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save(ambulance=ambulance)
            return Response({'message': 'Objeto criado com sucesso', 'data': serializer.data}, status=status.HTTP_201_CREATED )
        except ValidationError as e:
            return Response({'message': 'Erro de validação', 'errors': e.detail}, status=status.HTTP_400_BAD_REQUEST)


    def update(self, request, *args, **kwargs):
        # Personalize aqui o código para o método PUT
        try:
            paramedic = self.get_object()
            ambulance = self.get_ambulance(request.data.get("ambulance"))
            serializer = ParamedicSerializer(paramedic, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save(ambulance=ambulance)
            return Response({'message': 'Objeto atualizado com sucesso', 'data': serializer.data})
        except ValidationError as e:
            return Response({'message': 'Erro de validação', 'errors': e.detail}, status=status.HTTP_400_BAD_REQUEST)


    
    def partial_update(self, request, *args, **kwargs):
        # Personalize aqui o código para o método PATCH
        try:
            paramedic = self.get_object()
            ambulance = self.get_ambulance(request.data.get("ambulance"))
            serializer = ParamedicSerializer(paramedic, data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save(ambulance = ambulance)
            return Response({'message': 'Objeto atualizado parcialmente com sucesso', 'data': serializer.data})
        except ValidationError as e:
            return Response({'message': 'Erro de validação', 'errors': e.detail}, status=status.HTTP_400_BAD_REQUEST)









