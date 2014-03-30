from django.shortcuts import render
from django.views.generic import (TemplateView, CreateView, 
            UpdateView, DetailView, ListView, FormView, DeleteView)
from django.core.urlresolvers import reverse
from django.forms import ModelForm

from .models import API, Klass, Instance

#TODO refactor classes to be more DRY
#TODO find a way for the URL reversing to be more DRY

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


class UserPageView(ListView):
    model = API
    template_name = "datasets/api/list.html"

user_page = UserPageView.as_view()

delete_api = nope


class KlassCreateView(CreateView):
    model = Klass
    template_name = "datasets/klass/new.html"
    
    def get_success_url(self):
        return reverse('view_api',args=(self.request.user.pk, self.object.api.slug,))

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
        return reverse('view_api',args=(self.request.user.pk, self.object.api.slug,))

edit_klass = KlassEditView.as_view()

delete_klass = nope

class InstanceViewMixin: 
    model = Instance

    def get_context_data(self, **kwargs):
        data = super(InstanceViewMixin, self).get_context_data(**kwargs)
        data['klass'] = self.get_klass()
        data['api'] = self.get_api()
        return data

    def get_klass(self): #TODO make it a one-time request
        return Klass.objects.get(slug=self.kwargs['klass_slug'])

    def get_api(self):
        return self.get_klass().api

    def get_queryset(self):
        return Instance.objects.filter(
            klass=self.get_klass(),
            klass__api=self.get_api(),
        ).select_related()

#TODO add CRSF token for delete button
class InstanceListView(InstanceViewMixin, ListView):
    template_name = "datasets/instance/list.html"


class InstanceCreateView(InstanceViewMixin, CreateView):
    template_name = "datasets/instance/new.html"

    def get_success_url(self):
        return reverse('instance_list',args=(
            self.request.user.pk,
            self.object.klass.api.slug,
            self.object.klass.slug))

class InstanceEditView(UpdateView):
    model = Instance
    pk_url_kwarg = 'instance_pk'
    template_name = "datasets/instance/edit.html"

    def get_success_url(self):
        return reverse('instance_list',args=(
            self.request.user.pk,
            self.object.klass.api.slug,
            self.object.klass.slug))

class InstanceDeleteView(DeleteView):
    model = Instance
    pk_url_kwarg = 'instance_pk'

    def get_success_url(self):
        return reverse('instance_list',args=(
            self.request.user,
            self.object.klass.api.slug,
            self.object.klass.slug))


instance_list = InstanceListView.as_view()
new_instance = InstanceCreateView.as_view()
edit_instance = InstanceEditView.as_view()
delete_instance = InstanceDeleteView.as_view()

delete_all_instances = nope

user_profile = nope
