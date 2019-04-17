from frontend import views
# import requests
from django.views.generic.base import TemplateView

APP_TEMPLATE_DIR = 'frontend/'
API_ROOT_URL = 'http://localhost:8000/api/v1/'


class HomeView(TemplateView):

    template_name = APP_TEMPLATE_DIR + "home.html"

    def get_context_data(self, **kwargs):
        """
        Override the get_context_data method to add new data to the
        context dictionary that is passed to the template
        """
        context = super().get_context_data(**kwargs)
        # context['greeting'] = 'Welcome to the Front End!'
        # send a request to the api to retrieve the list of pilots
        # car_list = self.get_from_api('cars')
        # add pilot_list key to the context dictionary so we can use it
        # in the template
        # context['car_list'] = car_list
        return context

    def get_from_api(self, url):
        """
        Sends a get requests to API_ROOT_URL/url
        @param url : string
        @return json api response
        """
        # response = requests.get(API_ROOT_URL + url)
        # data = response.json()
        # return data
        return
