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

#TODO namespace URLs and move them to
#TODO rename API to Dabaset

SLUG_REGEX = '[a-zA-Z0-9]+'

urlpatterns += patterns('datasets.views', 
        url(r'^$', 'home', name="home"),
        url(r'^new/$', 'new_api', name="new_api"),

        #TODO move this inside user/xxx/api/xxx/class/xxx/instances/
        url(r'^instances/(?P<instance_pk>\d+)/', include(patterns('datasets.views',
            url(r'edit/$', 'edit_instance', name="edit_instance"),
            url(r'delete/$', 'delete_instance', name="delete_instance"),
            ))),

        url(r'^user/(?P<user_pk>\d+)/', include(patterns('datasets.views',
            url(r'^$', 'user_page', name='user_page'), 
            url(r'^api-admin/(?P<api_slug>%s)/' % SLUG_REGEX, include(patterns('datasets.views',
                url(r'^$', 'view_api', name="view_api"),
                url(r'^edit/$', 'edit_api', name="edit_api"),
                url(r'^delete/$', 'delete_api', name="delete_api"),
                url(r'^class/new$', 'new_klass', name="new_klass"),
                url(r'^class/(?P<klass_slug>%s)/' % SLUG_REGEX, include(patterns('datasets.views',
                    url(r'edit/$', 'edit_klass', name="edit_klass"),
                    url(r'delete/$', 'delete_klass', name="delete_klass"),

                    url(r'instances/$', 'instance_list', name="instance_list"),
                    url(r'instances/new/$', 'new_instance', name="new_instance"),
                    url(r'instances/delete_all/$', 'delete_all_instances', name="delete_all_instances"),
                    ))),
                ))),
            ))),
        )

