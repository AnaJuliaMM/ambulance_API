# Import necessary modules from the Django Rest Framework
from rest_framework import serializers

# Import the ParamedicEntity model
from ambulance.models.paramedicEntity import ParamedicEntity

class ParamedicSerializer(serializers.ModelSerializer):
    """
    A serializer class for ParamedicEntity instances that extends the ModelSerializer class

    It contains an internal class called Meta
    """

    class Meta:
        """
        Metadata options for the serializer.

        Attributes:
            model (Model): The model associated with this serializer (ParamedicEntity).
            fields (str): A special string '__all__' to indicate that all fields from the model should be included in serialization.
        """
        model = ParamedicEntity
        fields = '__all__'
