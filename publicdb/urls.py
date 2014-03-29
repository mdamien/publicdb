from django.conf.urls import patterns, include, url

from datasets.views import HomeView, CreateAPIView, APIDetailView

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('', 
    url(r'^$', HomeView.as_view(), name="home"),
    url(r'^new/$', CreateAPIView.as_view(), name="new_api"),
    url(r'^(?P<slug>\w+)/infos', APIDetailView.as_view(), name="view_api"),

    url(r'^logout/$', 'django.contrib.auth.views.logout', { 'next_page':"/" }),
    url(r'^admin/', include(admin.site.urls)),
)
