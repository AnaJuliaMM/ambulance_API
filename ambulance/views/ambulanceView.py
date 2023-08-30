#Function Based View
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse

from ambulance.models.ambulanceEntity import AmbulanceEntity
from ambulance.serializers.ambulanceSerializer import AmbulanceSerializer



@api_view(['GET'])
def getAmbulances(request):
    queryset = AmbulanceEntity.objects.all() 
    serializer_class = AmbulanceSerializer(queryset, many=True)
    return JsonResponse(serializer_class.data, safe=False)





@api_view(['POST'])
def postAmbulance():
    pass