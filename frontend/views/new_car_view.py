from frontend.constants import APP_TEMPLATE_DIR, API_ROOT_URL
# import requests
from django.views.generic.base import TemplateView


class NewCarView(TemplateView):

    template_name = APP_TEMPLATE_DIR + "new-car.html"

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
