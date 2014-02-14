from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

#urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'testproj.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # url(r'^admin/', include(admin.site.urls)),

urlpatterns = patterns('loginCount.views',
    url(r'^$', 'default'),
    #url(r'^(?P<poll_id>\d+)/$', 'detail'),
    #url(r'^(?P<poll_id>\d+)/results/$', 'results'),
#    url(r'^(?P<poll_id>\d+)/vote/$', 'vote'),
)

urlpatterns += patterns('',
    url(r'^admin/', include(admin.site.urls)),
)

