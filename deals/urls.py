from django.conf.urls import patterns, include, url
from django.contrib import admin

from .views import home_view

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', home_view),
    url(r'^admin/', admin.site.urls),
)
