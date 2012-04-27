from django.views.generic import TemplateView, FormView, UpdateView, CreateView, DetailView
from app.timesheet.models import TimeEntry
from app.timesheet.forms import TimeEntryForm, TimeClockOutForm, TimeEntryCommentForm
from app.ext.views import JSONView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from datetime import datetime
from django.template.defaultfilters import escape
import sys
from django.core import serializers
from django.middleware import csrf

class TimeView(TemplateView):
    template_name = "timesheet/index.html"

    def get_context_data(self, **kwargs):
        kwargs = super(TimeView, self).get_context_data(**kwargs)
        active_sessions = TimeEntry.objects.filter(stop_time__isnull=True)

        if active_sessions:
            session = active_sessions[0]
        else:
            session = None

        kwargs.update({'times': TimeEntry.objects.all, 'form_create': TimeEntryForm, 'form_clockout': TimeClockOutForm, 'active_session': session})
        return kwargs

class TimeClockInView(JSONView):

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(TimeClockInView, self).dispatch(*args, **kwargs)

    def process(self, request, *args, **kwargs):
        if request.user:
            current_sessions = TimeEntry.objects.filter(stop_time__isnull=True)

            if current_sessions:
                return {'status': "info", 'message': "You are currently recording a session.", 'data': current_sessions} 
            else:
                ticket = TimeEntry(start_time=datetime.today(), user=request.user)
                ticket.save()
                return {'status': "success", 'data': serializers.serialize('json', [ticket])}
        else:
            return {'status': "error", 'message': "Something went wrong!"}

class TimeClockOutView(JSONView):
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(TimeClockOutView, self).dispatch(*args, **kwargs)
    
    def process(self, request, *args, **kwargs):
        if request.user and request.POST:
            entry_id = kwargs['entry_id']

            if not entry_id:
                return {'status': "error", "message": "Something went wrong!"}
            
            try:
                entry_id = int(entry_id)
            except ValueError: 
                return {'status': "error", "message": "Something went wrong!"}
            
            try:
                entry = TimeEntry.objects.get(id=entry_id)

                if entry.stop_time:
                    return {'status': "error", "message": "Something went wrong!"}

                entry.stop_time = datetime.today()
                entry.category = escape(request.POST['category'])
                entry.save()
            except Exception as inst:
                return {'status': "error", "message": "Something went wrong! " + str(inst)}

            return {'status': "success", "data": serializers.serialize('json', [entry])}
        else:
            return {'status': "error", "message": "Something went wrong!"}

class TimeDeleteEntryView(JSONView):
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(TimeDeleteEntryView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return self.render_to_response({'status': "error", "message": "Something went wrong."})

    def delete(self, request, *args, **kwargs):
        return self.render_to_response(self.remove_entry(kwargs['entry_id']))

    def remove_entry(self, entry_id):
        try:
            entry_id = int(entry_id)
            entry = TimeEntry.objects.get(id=entry_id)
            entry.delete()
        except Exception as inst:
            return {'status': "error", "message": "Something went wrong! " + str(inst)}

        return {'status': 'success', 'data': serializers.serialize('json', [entry])}

    def process(self, request, *args, **kwargs):
        return {}

class TimeCreateEntryView(CreateView):
    form_class = TimeEntryForm
    template_name = "timesheet/create.html"
    model = TimeEntry
    success_url = "/time/"

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(TimeCreateEntryView, self).dispatch(*args, **kwargs)
    
    def get_context_data(self, **kwargs):
        kwargs = super(TimeCreateEntryView, self).get_context_data(**kwargs)
        active_sessions = TimeEntry.objects.filter(stop_time__isnull=True)

        if active_sessions:
            session = active_sessions[0]
        else:
            session = None

        kwargs.update({'times': TimeEntry.objects.all, 'form_clockout': TimeClockOutForm, 'active_session': session})
        return kwargs

class TimeUpdateEntryView(UpdateView):
    model = TimeEntry
    form_class = TimeEntryForm
    template_name = "timesheet/create.html"
    success_url = "/time/"

class TimeDetailEntryView(DetailView):
    model = TimeEntry

    def get_context_data(self, **kwargs):
        kwargs = super(TimeDetailEntryView, self).get_context_data(**kwargs)
        active_sessions = TimeEntry.objects.filter(stop_time__isnull=True)

        if active_sessions:
            session = active_sessions[0]
        else:
            session = None

        kwargs.update({
            'times': TimeEntry.objects.all, 
            'form_create': TimeEntryForm, 
            'form_clockout': TimeClockOutForm, 
            'active_session': session,
            'form_comment': TimeEntryCommentForm
        })
        return kwargs
