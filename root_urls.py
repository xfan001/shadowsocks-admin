from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    # url(r'', TemplateView.as_view("")),
    # Examples:
    # url(r'^$', 'ssadmin.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

)
