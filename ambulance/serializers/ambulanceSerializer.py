from rest_framework import serializers
from ambulance.models.ambulanceEntity import AmbulanceEntity
from ambulance.serializers.paramedicSerializer import ParamedicSerializer

class AmbulanceSerializer(serializers.ModelSerializer):
    # Ou para paramedics = serializers.StringRelatedField(many=True) pegar a usar __str__()
    paramedics = ParamedicSerializer(many=True, read_only = True) 

    class Meta:
        model = AmbulanceEntity
        fields = '__all__'