from django.db import models
from django_countries.fields import CountryField
    
# Create your models here.

class Member(models.Model):
    Username = models.CharField(max_length=32)
    Description = models.CharField(max_length=32)
    Age = models.IntegerField(default=0)
    Country = CountryField()
    Hobbies = models.CharField(max_length=128)
    Question1 = models.CharField(max_length=128)
    Question2 = models.CharField(max_length=128)
    Question3 = models.CharField(max_length=128)
    Approved = models.BooleanField(default=False)
    bg = models.CharField(max_length=32, default="netherrack")


    def __str__(self):
        return f"{self.Username} (Age: {self.Age}) - [Approved: {self.Approved}]"