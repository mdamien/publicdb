from django.conf.urls import patterns, include, url

from datasets.views import HomeView, APICreateView, APIDetailView, APIEditView, APIListView

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('', 
    url(r'^$', HomeView.as_view(), name="home"),
    url(r'^new/$', APICreateView.as_view(), name="new_api"),
    url(r'^list/', APIListView.as_view(), name="api_list"),
    url(r'^(?P<slug>\w+)/infos', APIDetailView.as_view(), name="view_api"),
    url(r'^(?P<slug>\w+)/edit', APIEditView.as_view(), name="edit_api"),

    url(r'^logout/$', 'django.contrib.auth.views.logout', { 'next_page':"/" }),
    url(r'^admin/', include(admin.site.urls)),
)
