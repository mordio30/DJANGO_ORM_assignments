from django.db import models

# Create your models here.

class Client(models.Model):
    account_type = models.CharField(max_length=255, null=False, blank=False) 
    email = models.CharField(max_length=255, null=False, blank=False) 
    active = models.BooleanField(default=True)

class Video(models.Model):
    title = models.CharField(max_length=255, null=False, blank=False) 
    in_stock = models.PositiveBigIntegerField(unique=True, null=False, blank=False)
    rating = models.CharField(max_length=255, null=False, blank=False)

class Person(models.Model):
    first_name = models.CharField(max_length=255, null=False, blank=False) 
    last_name = models.CharField(max_length=255, null=False, blank=False) 
    middle_initial = models.CharField(max_length=2, null=False, blank=False)
    age = models.PositiveBigIntegerField(unique=True, null=False, blank=False)

class Address(models.Model):
    street = models.CharField(max_length=255, null=False, blank=False) 
    zipcode = models.PositiveBigIntegerField(unique=True, null=False, blank=False)
    state = models.CharField(max_length=255, null=False, blank=False) 
    app_num = models.PositiveBigIntegerField(unique=True, null=False, blank=False)
    
class Store(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False) 
    number_of_employees = models.PositiveBigIntegerField(unique=True, null=False, blank=False)
    rating = models.FloatField()
    owner = models.PositiveBigIntegerField(unique=True, null=False, blank=False)