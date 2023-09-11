from rest_framework import serializers
from ambulance.models.ambulanceEntity import AmbulanceEntity
from ambulance.serializers.paramedicSerializer import ParamedicSerializer

#Class used to serialize the Ambulances objects 
class AmbulanceSerializer(serializers.ModelSerializer):
    # Ou para paramedics = serializers.StringRelatedField(many=True) pegar a usar __str__()
    paramedics = ParamedicSerializer(many=True, read_only = True) 

    #Internal class with the fields that can be serialized ??
    class Meta:
        #The class model of the objects serialized 
        model = AmbulanceEntity
        # What field from the objects can be serialized or deserialized
        fields = '__all__'