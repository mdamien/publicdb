from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, DetailView 
from django.core.urlresolvers import reverse

from .models import API

class HomeView(TemplateView):
    template_name = "home.html"

class CreateAPIView(CreateView):
    model = API
    template_name = "datasets/new_api.html"

class APIDetailView(DetailView):
    model = API
    template_name = "datasets/view_api.html"
    context_obj = "api"
