from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('solo.views',
    url(r'^add/$', 'add', name='add'),
    url(r'^edit/(?P<slug>[-\w]+)/$', 'edit', name='edit'),
    url(r'^$', 'page', name='home'),
    url(r'^(?P<page_number>\d+)/$', 'page', name='page'),
    url(r'^(?P<slug>[-\w]+)/$', 'detail', name='detail')
)
