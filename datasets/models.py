from django.db import models
from django.contrib.auth.models import User
from django_extensions.db.fields import json

class API(models.Model):
    "A set of dataset. ex: Movie API with Movies, Ratings, Users, ..."
    name = models.CharField(max_length=30)
    slug = models.SlugField()
    owner = models.ForeignKey(User)

    def __str__(self):
        return self.name

class Klass(models.Model):
    "A representation of a class of data. ex:Book, Websites, Places, Tickets,.."
    api = models.ForeignKey(API)
    name = models.CharField(max_length=30)
    slug = models.SlugField()
    meta = json.JSONField() #Validation, plural, fields,...

    def __str__(self):
        return self.name

class Instance(models.Model):
    "A concrete data instance of a class of data. ex: Batman, Superman, Carott,.." 
    klass = models.ForeignKey(Klass)
    data = json.JSONField()

    def __str__(self):
        return "%s's instance" % self.klass.name 

