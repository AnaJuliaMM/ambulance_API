# Import necessary modules from Django
from django.db import models

class AmbulanceEntity(models.Model):
    """
    Model class for representing Ambulance entities.

    Attributes:
        chassi_code (CharField): The chassis code of the ambulance (max length: 17 characters).
        license_plate (CharField): The license plate of the ambulance (max length: 7 characters).
        base (CharField): The base location of the ambulance (max length: 50 characters).
        type (CharField): The type of ambulance, selected from predefined choices.
        is_avaiable (BooleanField): A flag indicating if the ambulance is available for service or not.

    Methods:
        __str__: Returns a string representation of the ambulance entity.
    """

    # Predefined choices for ambulance types
    types = [
        ("a", "Basic Life Support Ambulance"),
        ("b", "Intermediate Life Support Ambulance"),
        ("c", "Advanced Life Support Ambulance")
    ]

    chassi_code = models.CharField(max_length=17)
    license_plate = models.CharField(max_length=7)
    base = models.CharField(max_length=50)
    type = models.CharField(choices=types, max_length=100)
    is_avaiable = models.BooleanField()

    def __str__(self):
        """
        Returns a human-readable string representation of the ambulance entity.

        Example:
        Ambulance- license plate = ABC123, type = Basic Life Support Ambulance, status = Available
        """
        status = "Available" if self.is_avaiable else "Not available"
        return f'license plate = {self.license_plate}, type = {self.get_type_display()}, status = {status}'
