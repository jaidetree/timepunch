from django import http
from django.utils import simplejson as json
from django.views.generic.base import View

class JSONResponseMixin(object):
    def render_to_response(self, context):
        "Returns a JSON response containing 'context' as payload"
        return self.get_json_response(self.convert_context_to_json(context))

    def get_json_response(self, content, **httpresponse_kwargs):
        "Construct an `HttpResponse` object."
        return http.HttpResponse(content, content_type='application/json', **httpresponse_kwargs)

    def convert_context_to_json(self, context):
        "Convert the context dictionary into a JSON object"
        return json.dumps(context)

class JSONView(JSONResponseMixin, View):
    def get(self, request, *args, **kwargs):
        response = self.process(request, *args, **kwargs)
        return self.render_to_response(response)

    def post(self, request, *args, **kwargs):
        response = self.process(request, *args, **kwargs)
        return self.render_to_response(response)
