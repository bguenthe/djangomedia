from django.db import models

class Country(models.Model):
    country = models.CharField(max_length=200)
   
    def __str__(self):
        return self.country

class Vote(models.Model):
    country = models.ForeignKey(Country)
    name =  models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.name