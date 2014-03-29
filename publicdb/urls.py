from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^logout/$', 'django.contrib.auth.views.logout', { 'next_page':"/" }),
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += patterns('datasets.views', 
    url(r'^$', 'home', name="home"),
    url(r'^new/$', 'new_api', name="new_api"),
    url(r'^list/', 'api_list', name="api_list"),

    #TODO user profile user/<username>/ with api list
    url(r'^(?P<slug>\w+)/', include(patterns('datasets.views',
        url(r'^$', 'view_api', name="view_api"),
        url(r'^edit/', 'edit_api', name="edit_api"),
        #TODO Delete API
        #TODO CRUD Klasses
        #TODO CRUB Instances
    ))),
)

