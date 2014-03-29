from django.contrib import admin
from .models import API, Klass, Instance

admin.site.register((API, Klass, Instance))
