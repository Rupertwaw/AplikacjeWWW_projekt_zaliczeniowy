from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)

class Location(models.Model):
    name = models.CharField(max_length=100)
    floor = models.IntegerField(null=True, blank=True)

class Employee(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
   
class Device(models.Model):
    name = models.CharField(max_length=100)
    serial_number = models.CharField(max_length=100, unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True)
    assigned_to = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True, blank=True)
    purchase_date = models.DateField()

