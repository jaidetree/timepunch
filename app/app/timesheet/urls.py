from django.conf.urls import patterns, include, url
from app.timesheet.views import TimeView, TimeClockInView, TimeClockOutView, TimeDeleteEntryView, TimeCreateEntryView, TimeUpdateEntryView, TimeDetailEntryView

urlpatterns = patterns( 'time',
    url(r'^$', TimeView.as_view(), name="time.index"),
    url(r'in/$', TimeClockInView.as_view(), name="time.clockin"),
    url(r'out/(?P<entry_id>[\d]+)/$', TimeClockOutView.as_view(), name="time.clockout"),
    url(r'delete/(?P<entry_id>[\d]+)/$', TimeDeleteEntryView.as_view(), name="time.delete"),
    url(r'edit/(?P<pk>[\d]+)/$', TimeUpdateEntryView.as_view(), name="time.update"),
    url(r'create/$', TimeCreateEntryView.as_view(), name="time.create"),
    url(r'entry/(?P<pk>[\d]+)/$', TimeDetailEntryView.as_view(), name="time.show"),
    url(r'comments/', include('django.contrib.comments.urls')),
)
