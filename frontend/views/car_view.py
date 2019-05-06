"""
frontend/views/car_view.py
Author: Kevin Booth
Last Updated: 5/1/2019
"""
from frontend.constants import APP_TEMPLATE_DIR, API_ROOT_URL
from frontend.views.api_helper import APIHelper
from django.views.generic.base import TemplateView
from django.shortcuts import render
from frontend.forms import CompleteTaskForm


class CarView(TemplateView):
    """
    Class that handles the car detail frontend view
    GET - Returns default template
    POST - Sends complete date for a task
    """
    template_name = APP_TEMPLATE_DIR + "car.html"

    def get_context_data(self, id, **kwargs):
        """
        Override the get_context_data method to add new data to the
        context dictionary that is passed to the template
        """
        context = super().get_context_data(**kwargs)
        car = APIHelper.get_from_api('car/' + id,
                                     self.request.user.auth_token)
        task_list = APIHelper.get_from_api('car/' + id + '/tasks/',
                                           self.request.user.auth_token)
        part_list = APIHelper.get_from_api('parts/',
                                           self.request.user.auth_token)

        context['car'] = car
        context['task_list'] = task_list
        context['part_list'] = part_list

        return context

    def post(self, request, id, **kwargs):
        """
        Used to complete a task
        """
        form = CompleteTaskForm(self.request.POST)
        if form.is_valid():
            task_id = request.GET.get('task_id')
            task = APIHelper.get_from_api('task/' + task_id,
                                          self.request.user.auth_token)
            task['completion_date'] = form.cleaned_data['completion_date']
            APIHelper.put_to_api('task/' + task_id,
                                 self.request.user.auth_token,
                                 task)
            context = self.get_context_data(id)
            context['message'] = 'Thank you, your task has been completed.'
            return render(request, self.template_name, context)
        else:
            return render(request, self.template_name)
