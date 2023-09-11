from django.db import models 
from ambulance.models.ambulanceEntity import AmbulanceEntity

# Class that represents the table Paramedic in the Data Base, this table contains the employees that are paramedics
class ParamedicEntity(models.Model):
    # Paramedic table columns: 
   
    name = models.CharField(max_length=255)
    # Foreign Key that makes a Many to One relationship with Ambulance Table 
    ambulance = models.ForeignKey(AmbulanceEntity, related_name= 'paramedics', on_delete=models.CASCADE)
                                     
   
    # Action : method used to print a instances of this class as a string
    # Return: returns a String with the class name and its name
    def __str__(self):
        return self.name
   