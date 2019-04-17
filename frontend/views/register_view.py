# import requests
from django.views.generic.base import TemplateView

APP_TEMPLATE_DIR = 'frontend/'
API_ROOT_URL = 'http://localhost:8000/api/v1/'


class RegisterView(TemplateView):

    template_name = APP_TEMPLATE_DIR + "register.html"

    def get_context_data(self, **kwargs):
        """
        Override the get_context_data method to add new data to the
        context dictionary that is passed to the template
        """
        context = super().get_context_data(**kwargs)
        return context

    def get_from_api(self, url):
        """
        Sends a get requests to API_ROOT_URL/url
        @param url : string
        @return json api response
        """
        return
