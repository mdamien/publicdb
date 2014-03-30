from tastypie.api import Api
from tastypie.resources import ModelResource

import datasets.models as models

class APIResource(ModelResource):
    class Meta:
        queryset = models.API.objects.all()


class KlassResource(ModelResource):
    class Meta:
        queryset = models.Klass.objects.all()


class InstanceResource(ModelResource):
    class Meta:
        queryset = models.Instance.objects.all()

api = Api(api_name='v1')

api.register(APIResource())
api.register(KlassResource())
api.register(InstanceResource())

