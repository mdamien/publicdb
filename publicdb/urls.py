from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from datasets.api import api

urlpatterns = patterns('',
    url(r'^api/', include(api.urls)),
    url(r'^logout/$', 'django.contrib.auth.views.logout', { 'next_page':"/" }),
    url('^login/$', 'datasets.views.nope', name="login"),
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += patterns('datasets.views', 
    url(r'^$', 'home', name="home"),
    url(r'^new/$', 'new_api', name="new_api"),
    url(r'^list/$', 'api_list', name="api_list"),

    url(r'^user/(?P<pk>\d+)/$', 'user_profile', name='user_profile'), 
    url(r'^(?P<api_slug>[-\w]+)/', include(patterns('datasets.views',
        url(r'^$', 'view_api', name="view_api"),
        url(r'^edit/$', 'edit_api', name="edit_api"),
        url(r'^delete/$', 'delete_api', name="delete_api"),
        url(r'^class/new$', 'new_klass', name="new_klass"),
        url(r'^class/(?P<klass_slug>[-\w]+)/', include(patterns('datasets.views',
            url(r'edit/$', 'edit_klass', name="edit_klass"),
            url(r'delete/$', 'delete_klass', name="delete_klass"),
            url(r'instances/$', 'instance_list', name="instance_list"),
            url(r'instance/new/$', 'new_instance', name="new_instance"),
            url(r'instance/delete_all/$', 'delete_all_instances', name="delete_all_instances"),
            url(r'instance/(?P<pk>\d>)/', include(patterns('datasets.views',
                url(r'edit/$', 'edit_instance', name="edit_instance"),
                url(r'delete/$', 'delete_instance', name="delete_instance"),
            ))),
        ))),
    ))),
)

