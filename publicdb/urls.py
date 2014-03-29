from django.conf.urls import patterns, include, url

from datasets.views import HomeView, APICreateView, APIDetailView, APIEditView, APIListView

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('', 
    url(r'^$', HomeView.as_view(), name="home"),
    url(r'^new/$', APICreateView.as_view(), name="new_api"),
    url(r'^list/', APIListView.as_view(), name="api_list"),
    url(r'^logout/$', 'django.contrib.auth.views.logout', { 'next_page':"/" }),
    url(r'^admin/', include(admin.site.urls)),

    #TODO user profile user/<username>/ with api list
    url(r'^(?P<slug>\w+)/', include(patterns('',
        url(r'^$', APIDetailView.as_view(), name="view_api"),
        url(r'^edit/', APIEditView.as_view(), name="edit_api"),
        #TODO CRUD Klasses
        #TODO CRUB Instances
    ))),
)

