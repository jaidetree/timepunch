from django.conf.urls import patterns, include, url
from app.views import Home

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'app.views.home', name='home'),
    # url(r'^app/', include('app.foo.urls')),

    url(r'^$', Home.as_view(), name='home'),
    url(r'^time/', include('app.timesheet.urls')),

    url(r'^accounts/login/$', 'django.contrib.auth.views.login'),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
