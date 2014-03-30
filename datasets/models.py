from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django_extensions.db.fields import json, CreationDateTimeField

#TODO own JSON Field
#TODO Timestamp the data [instance]

class API(models.Model):
    "A set of dataset. ex: Movie API with Movies, Ratings, Users, ..."
    name = models.CharField(max_length=30)
    slug = models.SlugField(unique=True)
    owner = models.ForeignKey(User)
    meta = json.JSONField(blank=True)
    created = CreationDateTimeField()

    def get_absolute_url(self):
        return reverse('view_api',args=(self.slug,))

    def __str__(self):
        return self.name

class Klass(models.Model):
    "A representation of a class of data. ex:Book, Websites, Places, Tickets,.."
    api = models.ForeignKey(API, related_name="klasses")
    name = models.CharField(max_length=30)
    slug = models.SlugField()
    meta = json.JSONField(blank=True)
    created = CreationDateTimeField()

    class Meta:
        unique_together = ("api", "slug")
    
    def __str__(self):
        return self.name

class Instance(models.Model):
    "A concrete data instance of a class of data. ex: Batman, Superman, Carott,.." 
    klass = models.ForeignKey(Klass,related_name='instances')
    data = json.JSONField()

    def __str__(self):
        return "%s's instance" % self.klass.name 

