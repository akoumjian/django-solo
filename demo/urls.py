from django.conf.urls.defaults import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic import TemplateView

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^markitup/', include('markitup.urls')),
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^about/', TemplateView.as_view(template_name='demo/about.html')),
    url(r'^', include('solo.urls')),
)

urlpatterns += staticfiles_urlpatterns()
