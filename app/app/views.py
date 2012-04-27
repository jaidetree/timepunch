from django.views.generic import TemplateView, RedirectView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

class Home(RedirectView):
    url = "/time/"

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(Home, self).dispatch(*args, **kwargs)

