from django.db import models

# Class that represents the table Ambulance in the Data Base
class AmbulanceEntity(models.Model): 
    #Structure with the possibles values of the field type
    types =[
        ("a", "Ambuância de Suporte Básico"),
        ("b", "Ambuância de Suporte Médio"),
        ("c", "Ambuância de Suporte Avançado")
    ]


    # Ambulance table columns 
    chassi_code = models.CharField(max_length=17)
    license_plate = models.CharField(max_length=7)

    # Field that contains the base or headquarter that the ambulance was registered
    base = models.CharField(max_length=50)

    # Field that is filled with one of the options of the above structure "types" 
    type = models.CharField(choices=types, max_length=100)

    #Boolean field - True: the ambulance is avaible, False: the ambulance is not avaible
    is_avaiable = models.BooleanField() 


    # Action: method used to print a instance of this class as a string
    # Return: returns a String with the class name, the ambulance type, the license plate and if it is avaible or not
    def __str__(self):
        return f'Ambulance: {self.type}, {self.license_plate}, {"Disponível" if self.is_avaiable else "Não disponível"}'
    