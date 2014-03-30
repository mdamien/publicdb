from tastypie.api import Api
from tastypie import fields
from tastypie.resources import ModelResource, ALL, ALL_WITH_RELATIONS

import datasets.models as models
from django.contrib.auth.models import User

class UserResource(ModelResource):
    class Meta:
        queryset = User.objects.all()
        filtering = {
            'pk': ['exact'],
            'username': ['exact'],
        }

class APIResource(ModelResource):
    owner = fields.ToOneField(UserResource,'owner')
    
    class Meta:
        queryset = models.API.objects.all()
        filtering = {
            'slug': ['exact'],
            'owner': ALL_WITH_RELATIONS
            }

class KlassResource(ModelResource):
    api = fields.ToOneField(APIResource, 'api')

    class Meta:
        queryset = models.Klass.objects.all()
        filtering = {
            'slug': ['exact'],
            'api': ALL_WITH_RELATIONS,
            }


class InstanceResource(ModelResource):
    klass = fields.ToOneField(KlassResource, 'klass')
    
    class Meta:
        queryset = models.Instance.objects.all()
        filtering = {
            'data': ALL,
            'modified': ALL,
            'created': ALL,
            'klass': ALL_WITH_RELATIONS,
            }


api = Api(api_name='v1')

api.register(APIResource())
api.register(KlassResource())
api.register(InstanceResource())

