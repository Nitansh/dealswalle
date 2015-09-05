from django.conf.urls import patterns, include, url
from django.contrib import admin

from .views import home_view, iles_view, privacy_view, aboutus_view, contactus_view

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', home_view),
    url(r'^admin/', admin.site.urls),
)
