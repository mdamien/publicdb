from django.shortcuts import render
from django.views.generic import (TemplateView, CreateView, 
            UpdateView, DetailView, ListView, FormView, DeleteView)
from django.core.urlresolvers import reverse, reverse_lazy
from django.forms import ModelForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import API, Klass, Instance, LIMITS
from django.core.exceptions import ValidationError

#TODO factorize functions to be more DRY

class HomeView(TemplateView):
    template_name = "home.html"

home = HomeView.as_view()
nope = TemplateView.as_view(template_name="nope.html")

class LoginRequiredMixin:
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(LoginRequiredMixin, self).dispatch(*args, **kwargs)


class APIForm(ModelForm):
    
    class Meta:
        model = API
        fields = ('name','slug')

    def clean(self):        
        if self.owner.api_set.count() >= LIMITS.API_PER_USER:
            raise ValidationError("A user can't have more than %d APIs" % LIMITS.API_PER_USER)
        return super(APIForm, self).clean()

    def save(self, force_insert=False, force_update=False, commit=True):
        m = super(APIForm, self).save(commit=False)
        m.owner = self.owner
        if commit:
            m.save()
        return m

class APICreateView(LoginRequiredMixin, CreateView):
    form_class = APIForm
    template_name = "datasets/api/new.html"
    slug_url_kwarg = "api_slug"

    def get_form(self, form_class):
        form = super(APICreateView, self).get_form(form_class)
        form.owner = self.request.user
        return form


new_api = APICreateView.as_view()

class APIEditView(LoginRequiredMixin, UpdateView):
    form_class = APIForm
    slug_url_kwarg = "api_slug"
    model = API
    template_name = "datasets/api/edit.html"

    def get_form(self, form_class):
        form = super(APIEditView, self).get_form(form_class)
        form.owner = self.request.user
        return form

    def get_queryset(self):
        return super(APIEditView, self).get_queryset().filter(owner=self.request.user)

edit_api = APIEditView.as_view()


class APIDetailView(LoginRequiredMixin, DetailView):
    model = API
    slug_url_kwarg = "api_slug"
    template_name = "datasets/api/view.html"

    def get_queryset(self):
        return super(APIDetailView, self).get_queryset().filter(owner=self.request.user)

view_api = APIDetailView.as_view()

class APIDeleteView(LoginRequiredMixin, DeleteView):
    model = API
    slug_url_kwarg = "api_slug"
    template_name = "datasets/api/delete.html"

    success_url = reverse_lazy('home')

    def get_queryset(self):
        return super(APIDeleteView, self).get_queryset().filter(owner=self.request.user)

delete_api = APIDeleteView.as_view()

class UserPageView(LoginRequiredMixin, ListView):
    model = API
    template_name = "datasets/api/list.html"

    def get_queryset(self):
        return super(UserPageView, self).get_queryset().filter(owner=self.request.user)

user_page = UserPageView.as_view()

class KlassForm(ModelForm):
    
    class Meta:
        model = Klass
        fields = ('name','slug')

    def clean(self):
        if self.api.klasses.count() >= LIMITS.KLASS_PER_API:
            raise ValidationError("An API can't have more than %d Classes" % LIMITS.KLASS_PER_API) 
        return super(KlassForm, self).clean()


    def save(self, force_insert=False, force_update=False, commit=True):
        m = super(KlassForm, self).save(commit=False)
        m.api = self.api
        if commit:
            m.save()
        return m


class KlassCreateView(LoginRequiredMixin, CreateView):
    model = Klass
    form_class = KlassForm
    template_name = "datasets/klass/new.html"

    def get_form(self, form_class):
        form = super(KlassCreateView, self).get_form(form_class)
        form.api = API.objects.get(slug=self.kwargs.get('api_slug'),
                owner=self.request.user)
        return form

    def get_success_url(self):
        return reverse('view_api',args=(self.request.user.pk, self.object.api.slug,))

new_klass = KlassCreateView.as_view()


class KlassEditView(LoginRequiredMixin, UpdateView):
    model = Klass
    form_class = KlassForm
    template_name = "datasets/klass/edit.html"

    def get_object(self):
        return Klass.objects.get(
            api__slug=self.kwargs['api_slug'],
            slug=self.kwargs['klass_slug'],
        )

    def get_form(self, form_class):
        form = super(KlassEditView, self).get_form(form_class)
        form.api = API.objects.get(slug=self.kwargs.get('api_slug'),
                owner=self.request.user)
        return form
    
    def get_success_url(self):
        return reverse('view_api',args=(self.request.user.pk, self.object.api.slug,))

    def get_queryset(self):
        return super(KlassEditView, self).get_queryset().filter(api__owner=self.request.user)

edit_klass = KlassEditView.as_view()

class DeleteKlassView(LoginRequiredMixin, DeleteView):
    model = Klass
    template_name = "datasets/klass/delete.html"

    def get_object(self):
        return Klass.objects.get(
            api__slug=self.kwargs['api_slug'],
            slug=self.kwargs['klass_slug'],
        )
    
    def get_success_url(self):
        return reverse('view_api',args=(self.request.user.pk, self.object.api.slug,))

delete_klass = DeleteKlassView.as_view()

class InstanceForm(ModelForm):
    
    class Meta:
        model = Instance
        fields = ('data',)

    def clean(self):        
        if self.klass.instances.count() >= LIMITS.INSTANCES_PER_KLASS:
            raise ValidationError("A Class can't have more than %s Instances" % LIMITS.INSTANCES_PER_KLASS)
        if len(self.data) > LIMITS.INSTANCE_DATA_LENGTH:
            raise ValidationError("An instance data can't have more than %d characters" % LIMITS.INSTANCE_DATA_LENGTH)
        return super(InstanceForm, self).clean()

    def save(self, force_insert=False, force_update=False, commit=True):
        m = super(InstanceForm, self).save(commit=False)
        m.klass = self.klass
        if commit:
            m.save()
        return m


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
            klass__api__owner=self.request.user,
            klass=self.get_klass(),
            klass__api=self.get_api(),
        ).select_related()

#TODO add CRSF token for delete button
class InstanceListView(InstanceViewMixin, ListView):
    template_name = "datasets/instance/list.html"

    def get_queryset(self):
        return super(InstanceListView, self).get_queryset().filter(klass__api__owner=self.request.user)

class InstanceCreateView(InstanceViewMixin, CreateView):
    template_name = "datasets/instance/new.html"
    form_class = InstanceForm

    def get_success_url(self):
        return reverse('instance_list',args=(
            self.request.user.pk,
            self.object.klass.api.slug,
            self.object.klass.slug))

    def get_form(self, form_class):
        form = super(InstanceCreateView, self).get_form(form_class)
        form.klass = self.get_klass()
        return form
    
    def get_queryset(self):
        return super(InstanceCreateView, self).get_queryset().filter(klass__api__owner=self.request.user)


class InstanceEditView(UpdateView):
    model = Instance
    pk_url_kwarg = 'instance_pk'
    template_name = "datasets/instance/edit.html"
    form_class = InstanceForm

    def get_success_url(self):
        return reverse('instance_list',args=(
            self.request.user.pk,
            self.object.klass.api.slug,
            self.object.klass.slug))

    def get_form(self, form_class):
        form = super(InstanceEditView, self).get_form(form_class)
        form.klass = self.object.klass
        return form
    
    def get_queryset(self):
        return super(InstanceEditView, self).get_queryset().filter(klass__api__owner=self.request.user)


class InstanceDeleteView(DeleteView):
    model = Instance
    pk_url_kwarg = 'instance_pk'

    def get_success_url(self):
        return reverse('instance_list',args=(
            self.request.user.pk,
            self.object.klass.api.slug,
            self.object.klass.slug))

    def get_queryset(self):
        return super(InstanceDeleteView, self).get_queryset().filter(klass__api__owner=self.request.user)

instance_list = InstanceListView.as_view()
new_instance = InstanceCreateView.as_view()
edit_instance = InstanceEditView.as_view()
delete_instance = InstanceDeleteView.as_view()

delete_all_instances = nope

user_profile = nope
