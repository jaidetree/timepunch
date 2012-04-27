from django.forms import ModelForm, SplitDateTimeWidget
from app.timesheet.models import TimeEntry
from django.forms import fields
from datetime import datetime
from django import forms
from django.contrib.comments.forms import CommentForm
from django.contrib.comments.models import Comment

class TimeEntryForm(ModelForm):
    DATE_FORMATS = (
        '%Y-%m-%d %I:%M %p',
        '%Y-%m-%d %I:%M:%S %p',
        '%Y-%m-%d %H:%M',        # '2006-10-25 14:30'
        '%Y-%m-%d %H:%M:%S',     # '2006-10-25 14:30'
        '%Y-%m-%d',              # '2006-10-25'
        '%m/%d/%Y %H:%M:%S',     # '10/25/2006 14:30:59'
        '%m/%d/%Y %H:%M',        # '10/25/2006 14:30'
        '%m/%d/%Y',              # '10/25/2006'
        '%m/%d/%y %H:%M:%S',     # '10/25/06 14:30:59'
        '%m/%d/%y %H:%M',        # '10/25/06 14:30'
        '%m/%d/%y',              # '10/25/06'
    )
    start_time = fields.DateTimeField(input_formats=DATE_FORMATS, widget=SplitDateTimeWidget(time_format="%I:%M %p"))
    stop_time = fields.DateTimeField(input_formats=DATE_FORMATS, widget=SplitDateTimeWidget(time_format="%I:%M %p"))
    class Meta:
        model = TimeEntry
        exclude = ('user',)
        fields = ('start_time', 'stop_time', 'category')
        widgets = {
                'start_time': SplitDateTimeWidget(),
                'stop_time': SplitDateTimeWidget(),
        }

class TimeClockOutForm(ModelForm):
    class Meta:
        model = TimeEntry
        exclude = ('start_time', 'stop_time', 'user')

class TimeEntryCommentForm(CommentForm):
    def get_comment_model(self):
        return Comment
