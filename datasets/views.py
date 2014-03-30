from django.shortcuts import render
from django.views.generic import (TemplateView, CreateView, 
            UpdateView, DetailView, ListView, FormView)
from django.core.urlresolvers import reverse
from django.forms import ModelForm

from .models import API, Klass, Instance

class HomeView(TemplateView):
    template_name = "home.html"

home = HomeView.as_view()
nope = TemplateView.as_view(template_name="nope.html")

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
    template_name = "datasets/api/new.html"
    slug_url_kwarg = "api_slug"

    def form_valid(self, form):
        form.owner = self.request.user
        form.meta = "{}"
        return super(APICreateView, self).form_valid(form)

new_api = APICreateView.as_view()


class APIEditView(UpdateView):
    form_class = APIForm
    slug_url_kwarg = "api_slug"
    model = API
    template_name = "datasets/api/edit.html"

    def form_valid(self, form):
        form.owner = self.request.user
        form.meta = "{}"
        return super(APIEditView, self).form_valid(form)

edit_api = APIEditView.as_view()


class APIDetailView(DetailView):
    model = API
    slug_url_kwarg = "api_slug"
    template_name = "datasets/api/view.html"

view_api = APIDetailView.as_view()


class APIListView(ListView):
    model = API
    template_name = "datasets/api/list.html"

api_list = APIListView.as_view()

delete_api = nope


class KlassCreateView(CreateView):
    model = Klass
    template_name = "datasets/klass/new.html"
    
    def get_success_url(self):
        return reverse('view_api',args=(self.object.api.slug,))

new_klass = KlassCreateView.as_view()


class KlassEditView(UpdateView):
    model = Klass
    template_name = "datasets/klass/edit.html"

    def get_object(self):
        return Klass.objects.get(
            api__slug=self.kwargs['api_slug'],
            slug=self.kwargs['klass_slug'],
        )

    def get_success_url(self):
        return reverse('view_api',args=(self.object.api.slug,))

edit_klass = KlassEditView.as_view()

delete_klass = nope

class InstanceListView(ListView):
    model = Instance
    template_name = "datasets/instance/list.html"

    def get_queryset(self):
        return Instance.objects.filter(
            klass__slug=self.kwargs['klass_slug'],
            klass__api__slug=self.kwargs['api_slug'],
        )

instance_list = InstanceListView.as_view()
new_instance = nope
edit_instance = nope
delete_instance = nope
delete_all_instances = nope

user_profile = nope
