from frontend.constants import APP_TEMPLATE_DIR, API_ROOT_URL
from frontend.views.api_helper import APIHelper
from django.views.generic.base import TemplateView
from django.shortcuts import render
# from frontend.forms import EditCarForm


class EditCarView(TemplateView):

    template_name = APP_TEMPLATE_DIR + "edit-car.html"

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