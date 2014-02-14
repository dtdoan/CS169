from django.contrib import admin
from django.conf.urls import patterns, include, url
from django.views.generic import DetailView, ListView
from user.models import User
admin.autodiscover()

urlpatterns = patterns('',
    '''
    url(r'^$',
        ListView.as_view(
            queryset=User.objects.order_by('password')[:5],
            context_object_name='whatisthis',
            template_name='loginCount/index.html')),
    url(r'^(?P<pk>\d+)/$',
        DetailView.as_view(
            model=User,
            template_name='loginCount/detail.html')),
        '''
                       
    url(r'^user/$', 'loginCount.views.client'),
    url(r'^user/login/$', 'loginCount.views.login'),
    url(r'^user/add/$', 'loginCount.views.add'),
)


urlpatterns += patterns('',
    url(r'^admin/', include(admin.site.urls)),
)


