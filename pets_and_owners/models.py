from django.db import models

# Create your models here.
class Owner(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)
    age = models.PositiveBigIntegerField(unique=True, null=False, blank=False)
    number_of_pets = models.PositiveBigIntegerField(unique=True, null=False, blank=False)

class Cat(models.Model):
    breed = models.CharField(max_length=255, null=False, blank=False)
    age = models.PositiveBigIntegerField(unique=True, null=False, blank=False)
    vaccinated = models.BooleanField(default=False)
    description = models.TextField(blank=True, null=True)
    name = models.CharField(max_length=255, null=False, blank=False)

class Bird(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)
    age = models.PositiveBigIntegerField(unique=True, null=False, blank=False)
    vaccinated = models.BooleanField(default=False)
    description = models.TextField(blank=True, null=True)
    species = models.CharField(max_length=255, null=False, blank=False)
    
    
class Dog(models.Model):
    age = models.PositiveBigIntegerField(unique=True, null=False, blank=False)
    name = models.CharField(max_length=255, null=False, blank=False) 
    vaccinated = models.BooleanField(default=False)
    breed = models.CharField(max_length=255, null=False, blank=False)
    description = models.TextField(blank=True, null=True)

class ExoticAnimal(models.Model):
    region_of_origin = models.CharField(max_length=255, null=False, blank=False) 
    name = models.CharField(max_length=255, null=False, blank=False) 
    age = models.PositiveBigIntegerField(unique=True, null=False, blank=False)
    type_of_animal = models.CharField(max_length=255, null=False, blank=False)
    vaccinated = models.BooleanField(default=False)
    
     
    
