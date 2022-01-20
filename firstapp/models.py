from django.db import models

class Employee(models.Model):
    FirstName=models.CharField(max_length=100)
    LastName=models.CharField(max_length=100)
    Gender=models.CharField(max_length=12)
    DOB=models.DateField()
    Salutation=models.CharField(max_length=100)
    Designation=models.CharField(max_length=100)
    Email=models.EmailField()
    Mobile=models.CharField(max_length=10)
    AddressLine1=models.CharField(max_length=50)
    AddressLine2=models.CharField(max_length=50)
    City=models.CharField(max_length=50)
    State=models.CharField(max_length=50)
    Pin=models.CharField(max_length=7)
    Country=models.CharField(max_length=50)
