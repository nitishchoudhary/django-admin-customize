from django.db import models

# Create your models here.

class Movie(models.Model):
    name = models.CharField(max_length=255)
    duration = models.PositiveIntegerField()
    release = models.PositiveIntegerField()

    def __str__(self):
        return self.name

class Customer(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    mobile_number = models.PositiveIntegerField()

    def __str__(self):
        return self.first_name +' '+ self.last_name
