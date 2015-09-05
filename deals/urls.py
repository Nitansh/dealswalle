from django.conf.urls import patterns, include, url
from django.contrib import admin

from .views import home_view, iles_view, privacy_view, aboutus_view, contactus_view

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'immigration.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', home_view),
    url(r'^call_us$', iles_view),
    url(r'^privacy$', privacy_view),
    url(r'^aboutus$', aboutus_view),
    url(r'^contactus$', contactus_view),
    url(r'^admin/', admin.site.urls),
)
