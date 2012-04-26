from django.conf.urls import patterns, include, url
from app.timesheet.views import TimeView, TimeCreateView, TimeClockInView, TimeClockOutView, TimeDeleteEntryView

urlpatterns = patterns( 'time',
    url(r'^$', TimeView.as_view(), name="time.index"),
    url(r'create/$', TimeCreateView.as_view(), name="time.create"),
    url(r'in/$', TimeClockInView.as_view(), name="time.clockin"),
    url(r'out/(?P<entry_id>[\d]+)/$', TimeClockOutView.as_view(), name="time.clockout"),
    url(r'delete/(?P<entry_id>[\d]+)/$', TimeDeleteEntryView.as_view(), name="time.delete"),
)
