from rest_framework import serializers
from ambulance.models.paramedicEntity import ParamedicEntity

class ParamedicSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParamedicEntity
        fields = '__all__'