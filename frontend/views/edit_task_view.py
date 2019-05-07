"""
Module that renders the edit task page
frontend/views/edit_task_view.py
Author: Kevin Booth
Last Updated: 5/1/2019
"""
from frontend.constants import APP_TEMPLATE_DIR, API_ROOT_URL
from frontend.views.api_helper import APIHelper
from django.views.generic.base import TemplateView
from django.shortcuts import render
from django.http import HttpResponseRedirect
from frontend.forms import NewTaskForm


class EditTaskView(TemplateView):
    """
    Class that handles the edit task frontend view
    GET - Returns default template
    POST - Sends edited task data to edit a task or delete a task
    """
    template_name = APP_TEMPLATE_DIR + "edit-task.html"

    def get_context_data(self, car_id, task_id, **kwargs):
        """
        Override the get_context_data method to add new data to the
        context dictionary that is passed to the template
        """
        context = super().get_context_data(**kwargs)
        car = APIHelper.get_from_api('car/' + car_id,
                                     self.request.user.auth_token)
        task = APIHelper.get_from_api('task/' + task_id,
                                      self.request.user.auth_token)
        context['car'] = car
        context['task'] = task

        return context

    def post(self, request, car_id, task_id, **kwargs):
        """
        Handles any incoming post requests pointing to this view specifically
        for editing a task and deleting a task
        """
        if request.POST.get("delete"):
            response = APIHelper.delete_from_api('task/' + task_id,
                                                 self.request.user.auth_token)
            return HttpResponseRedirect('/')
        else:
            context = {}
            form = NewTaskForm(self.request.POST)

            if form.is_valid():
                form.cleaned_data['car_id'] = car_id
                if form.cleaned_data.get('completion_date') == '':
                    form.cleaned_data['completion_date'] = None
                APIHelper.put_to_api('task/' + task_id,
                                     self.request.user.auth_token,
                                     form.cleaned_data)
                context = self.get_context_data(car_id, task_id)
                context['message'] = 'Thank you! Your task has been updated.'
                return render(request, self.template_name, context)
            else:
                context['message'] = 'There was an error with your request.'
                return render(request, self.template_name, context)
