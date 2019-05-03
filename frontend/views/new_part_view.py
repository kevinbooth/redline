from frontend.constants import APP_TEMPLATE_DIR, API_ROOT_URL
from frontend.views.api_helper import APIHelper
from django.views.generic.base import TemplateView
from django.shortcuts import render
from frontend.forms import NewPartForm


class NewPartView(TemplateView):

    template_name = APP_TEMPLATE_DIR + "new-part.html"

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
        part_list = APIHelper.get_from_api('parts/',
                                           self.request.user.auth_token)
        context['car'] = car
        context['task'] = task
        context['part_list'] = part_list

        return context

    def post(self, request, car_id, task_id, **kwargs):
        form = NewPartForm(self.request.POST)
        context = self.get_context_data(car_id, task_id)


        if form.is_valid():
            form.cleaned_data['task_id'] = task_id
            APIHelper.post_to_api('parts/',
                                  self.request.user.auth_token,
                                  form.cleaned_data)
            context['message'] = 'Thank you! Your part has been saved.'
            return render(request, self.template_name, context)
        else:
            context['message'] = 'There was an error with your request.'
            return render(request, self.template_name, context)
 
