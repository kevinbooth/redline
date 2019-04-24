from frontend.constants import APP_TEMPLATE_DIR, API_ROOT_URL
import requests
from django.views.generic.base import TemplateView


class CarView(TemplateView):

    template_name = APP_TEMPLATE_DIR + "car.html"

    def get_context_data(self, id, **kwargs):
        """
        Override the get_context_data method to add new data to the
        context dictionary that is passed to the template
        """
        context = super().get_context_data(**kwargs)
        car = self.get_from_api('car/' + id,
                                self.request.user.auth_token
                                )
        task_list = self.get_from_api(
                                      'car/' + id + '/tasks/',
                                      self.request.user.auth_token
                                      )
        part_list = self.get_from_api(
                                      'parts/',
                                      self.request.user.auth_token
                                      )
        context['car'] = car
        context['task_list'] = task_list
        context['part_list'] = part_list

        return context

    def get_from_api(self, url, auth):
        """
        Sends a get requests to API_ROOT_URL/url
        @param url : string
        @return json api response
        """
        response = requests.get(
                                API_ROOT_URL + url,
                                headers={'Authorization': 'Token ' + str(auth)}
                                )
        print(response)
        data = response.json()
        return data
