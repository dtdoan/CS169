from django.contrib import admin
from django.conf.urls import patterns, include, url
from django.views.generic import DetailView, ListView
from user.models import User
admin.autodiscover()

urlpatterns = patterns('',
                       
    url(r'^user/login$', 'loginCount.views.login'),
    url(r'^user/add$', 'loginCount.views.add'),
)


urlpatterns += patterns('',
    url(r'^admin/', include(admin.site.urls)),
)


