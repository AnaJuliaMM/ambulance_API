"""
This module defines the ParamedicEntity model, representing paramedics in the system.
"""

# Import necessary modules from Django
from django.db import models

# Import the AmbulanceEntity model to establish a ForeignKey relationship
from ambulance.models.ambulanceEntity import AmbulanceEntity

class ParamedicEntity(models.Model):
    """
    Model class for representing Paramedic entities.

    Attributes:
        name (CharField): The name of the paramedic (max length: 255 characters).
        ambulance (ForeignKey): A ForeignKey relationship to the AmbulanceEntity model,
                                establishing a connection between paramedics and ambulances.

    Methods:
        __str__: Returns a string representation of the paramedic entity.
    """

    name = models.CharField(max_length=255)
    
    # Establish a ForeignKey relationship with AmbulanceEntity, allowing each paramedic to be associated with an ambulance
    ambulance = models.ForeignKey(AmbulanceEntity,related_name='paramedics',on_delete=models.CASCADE)

    def __str__(self):
        """
        Returns a human-readable string representation of the paramedic entity.
        """
        return self.name
