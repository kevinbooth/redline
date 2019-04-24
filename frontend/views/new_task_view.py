from frontend.constants import APP_TEMPLATE_DIR, API_ROOT_URL
from frontend.views.api_helper import APIHelper
from django.views.generic.base import TemplateView
from django.shortcuts import render
from frontend.forms import NewTaskForm


class NewTaskView(TemplateView):

    template_name = APP_TEMPLATE_DIR + "new-task.html"

    def get_context_data(self, id, **kwargs):
        """
        Override the get_context_data method to add new data to the
        context dictionary that is passed to the template
        """
        context = super().get_context_data(**kwargs)
        car = APIHelper.get_from_api('car/' + id,
                                     self.request.user.auth_token)
        context['car'] = car

        return context

    def post(self, request, id, **kwargs):
        context = self.get_context_data(id)
        form = NewTaskForm(self.request.POST)

        if form.is_valid():
            form.cleaned_data['car_id'] = id
            if form.cleaned_data.get('completion_date') == '':
                form.cleaned_data['completion_date'] = None
            APIHelper.post_to_api('car/' + id + '/tasks/',
                                  self.request.user.auth_token,
                                  form.cleaned_data)
            context['message'] = 'Thank you! Your task has been saved.'
            return render(request, self.template_name, context)
        else:
            context['message'] = 'There was an error with your request.'
            return render(request, self.template_name, context)
