from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'videochat.views.home', name='home'),
    # url(r'^videochat/', include('videochat.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'videochat.views.home', name='home'),
    
    # url(r'^admin/', admin.site.urls),
	url('^meeting/$', 'videochat.views.meeting'),
	url('^landing/$', 'videochat.views.landing'),
	#url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': '/Users/minqi/projects/kiwi/videochat/static'}),
)
