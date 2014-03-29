from django.shortcuts import render
from django.views.generic import (TemplateView, CreateView, 
            UpdateView, DetailView, ListView, FormView)
from django.core.urlresolvers import reverse
from django.forms import ModelForm

from .models import API, Klass

class APIForm(ModelForm):
    
    class Meta:
        model = API
        fields = ('name','slug')

    def save(self, force_insert=False, force_update=False, commit=True):
        m = super(APIForm, self).save(commit=False)
        m.owner = self.owner
        m.meta = self.meta
        if commit:
            m.save()
        return m


class APICreateView(CreateView):
    form_class = APIForm
    template_name = "datasets/new_api.html"

    def form_valid(self, form):
        form.owner = self.request.user
        form.meta = "{}"
        return super(APICreateView, self).form_valid(form)


class APIDetailView(DetailView):
    model = API
    template_name = "datasets/view_api.html"


class HomeView(TemplateView):
    template_name = "home.html"


class APIEditView(UpdateView):
    form_class = APIForm
    model = API
    template_name = "datasets/edit_api.html"

    def form_valid(self, form):
        form.owner = self.request.user
        form.meta = "{}"
        return super(APIEditView, self).form_valid(form)

class APIListView(ListView):
    model = API
    template_name = "datasets/list_apis.html"


