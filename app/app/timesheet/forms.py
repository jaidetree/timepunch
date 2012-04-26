from django.forms import ModelForm
from app.timesheet.models import TimeEntry

class TimeEntryForm(ModelForm):
    class Meta:
        model = TimeEntry
        exclude = ('start_time', 'stop_time', 'user')
