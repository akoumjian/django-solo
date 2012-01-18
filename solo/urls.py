from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('solo.views',
    url(r'^$', 'page', name='home'),
    url(r'^(?P<page_number>\d+)/$', 'page', name='page'),
    url(r'^(?P<slug>\w+)/$', 'detail', name='detail')
)
