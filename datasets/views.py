from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, UpdateView, DetailView, ListView
from django.core.urlresolvers import reverse

from .models import API

class HomeView(TemplateView):
    template_name = "home.html"

class APICreateView(CreateView):
    model = API
    template_name = "datasets/new_api.html"

class APIDetailView(DetailView):
    model = API
    template_name = "datasets/view_api.html"

class APIEditView(UpdateView):
    model = API
    template_name = "datasets/edit_api.html"

class APIListView(ListView):
    model = API
    template_name = "datasets/list_apis.html"
