from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^$', 'appcore.views.homepage'),
    (r'^(?P<hashCode>[a-zA-Z0-9]{5})$', 'appcore.views.linkpage'),
    # Example:
    # (r'^msgfuse/', include('msgfuse.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
)
