from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from app.timesheet.models import TimeEntry

class Home(TemplateView):
    template_name = "home.html"

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(Home, self).dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        kwargs = super(Home, self).get_context_data(**kwargs)
        kwargs.update({'times': TimeEntry.objects.all, 'form': TimeForm})
        return kwargs

