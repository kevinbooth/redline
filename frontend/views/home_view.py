from frontend.constants import APP_TEMPLATE_DIR, API_ROOT_URL
from frontend.views.api_helper import APIHelper
import requests
from django.views.generic.base import TemplateView


class HomeView(TemplateView):

    template_name = APP_TEMPLATE_DIR + "home.html"

    def get_context_data(self, **kwargs):
        """
        Override the get_context_data method to add new data to the
        context dictionary that is passed to the template
        """
        context = super().get_context_data(**kwargs)
        car_list = APIHelper.get_from_api('cars/',
                                          self.request.user.auth_token)
        context['car_list'] = car_list

        return context
