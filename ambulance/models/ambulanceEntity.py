from django.db import models

#it's a table on teh Data Base
class AmbulanceEntity(models.Model): 
    chassi_code = models.CharField(max_length=17)
    license_plate = models.CharField(max_length=7)
    base = models.CharField(max_length=50)
    type = models.CharField(max_length=100)
    is_avaiable = models.BooleanField()

    def __str__(self):
        return f'Ambulance: {self.type}, {self.license_plate}, {"Disponível" if self.is_avaiable else "Não disponível"}'