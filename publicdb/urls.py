from django.conf.urls import patterns, include, url

from datasets.views import HomeView, CreateAPIView

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('', 
    url(r'^$', HomeView.as_view(), name="home"),
    url(r'^new/$', CreateAPIView.as_view(), name="new_api"),
    url(r'^admin/', include(admin.site.urls)),
)
