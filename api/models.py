from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

class Employee(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    role = models.CharField(max_length=75)
    phone_number = PhoneNumberField(unique = True, null = False, blank = False)

    
    def __str__(self):
        return self.first_name
