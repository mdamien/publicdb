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
    url(r'^list/$', 'api_list', name="api_list"),

    url(r'^user/(?P<username>\w+)/$', 'nope', name='user_profile'), 
    url(r'^(?P<api_slug>\w+)/', include(patterns('datasets.views',
        url(r'^$', 'view_api', name="view_api"),
        url(r'^edit/$', 'edit_api', name="edit_api"),
        url(r'^delete/$', 'nope', name="delete_api"),
        url(r'^class/new$', 'nope', name="new_klass"),
        url(r'^class/(?P<class_slug>\w+)/', include(patterns('datasets.views',
            url(r'edit/$', 'nope', name="edit_klass"),
            url(r'delete/$', 'nope', name="delete_klass"),
            url(r'instance/new/$', 'nope', name="new_instance"),
            url(r'instance/(?P<pk>\d>)/', include(patterns('datasets.views',
                url(r'edit/$', 'nope', name="edit_instance"),
                url(r'delete/$', 'nope', name="delete_instance"),
            ))),
        ))),
    ))),
)

