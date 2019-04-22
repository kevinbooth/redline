import requests
from django.views.generic.base import TemplateView
from django.shortcuts import render
from frontend.forms import NewTaskForm

APP_TEMPLATE_DIR = 'frontend/'
API_ROOT_URL = 'http://localhost:8000/api/v1/'


class NewTaskView(TemplateView):

    template_name = APP_TEMPLATE_DIR + "new-task.html"

    def get_context_data(self, id, **kwargs):
        """
        Override the get_context_data method to add new data to the
        context dictionary that is passed to the template
        """
        context = super().get_context_data(**kwargs)
        car = self.get_from_api('car/' + id,
                                self.request.user.auth_token
                                )
        context['car'] = car

        return context

    def post(self, request, id, **kwargs):
        context = self.get_context_data(id)
        form = NewTaskForm(self.request.POST)

        if form.is_valid():
            form.cleaned_data['car_id'] = id
            if form.cleaned_data.get('completion_date') == '':
                form.cleaned_data['completion_date'] = None
            self.post_to_api(
                             'car/' + id + '/tasks/',
                             self.request.user.auth_token,
                             form.cleaned_data
                             )
            context['message'] = 'Thank you! Your task has been saved.'                
            return render(request, self.template_name, context)
        else:
            context['message'] = 'There was an error with your request.'
            return render(request, self.template_name, context)

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
        data = response.json()
        return data

    def post_to_api(self, url, auth, data=''):
        """
        Sends a get requests to API_ROOT_URL/url
        @param url : string
        @param data : json (optional)
        @return json api response
        """
        response = requests.post(
                                 API_ROOT_URL + url,
                                 headers={
                                          'Authorization': 'Token ' +
                                          str(auth)
                                          },
                                 json=data
                                 )
        data = response.json()
        return data
