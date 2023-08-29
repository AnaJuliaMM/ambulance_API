from django.db import models 
from ambulance.models.ambulanceEntity import AmbulanceEntity


class ParamedicEntity(models.Model):
    name = models.CharField(max_length=255)
    ambulance = models.ForeignKey(AmbulanceEntity, related_name= 'paramedics', on_delete=models.CASCADE)
                                     

    def __str__(self):
        return self.name