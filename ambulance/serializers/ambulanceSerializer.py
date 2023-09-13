# Import necessary modules from the Django Rest Framework
from rest_framework import serializers

# Import the AmbulanceEntity model and ParamedicSerializer
from ambulance.models.ambulanceEntity import AmbulanceEntity
from ambulance.serializers.paramedicSerializer import ParamedicSerializer

class AmbulanceSerializer(serializers.ModelSerializer):
    """
    A serializer class for AmbulanceEntity instances that extends the ModelSerializer class

    Attributes:
        paramedics (SlugRelatedField): A field to represent related Paramedic objects by their names.

    It also contains an internal class called Meta
    """

    # Use SlugRelatedField to represent related Paramedic objects by their names
    paramedics = serializers.SlugRelatedField(slug_field="name", many=True, read_only=True)

    class Meta:
        """
        Metadata options for the serializer.

        Attributes:
            model (Model): The model associated with this serializer (AmbulanceEntity).
            fields (str): A special string '__all__' to indicate that all fields from the model should be included in serialization.
        """
        model = AmbulanceEntity
        fields = '__all__'
