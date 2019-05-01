"""
frontend/views/new_car_view.py
Author: Kevin Booth
Last Updated: 5/1/2019
"""
from frontend.constants import APP_TEMPLATE_DIR, API_ROOT_URL
from frontend.views.api_helper import APIHelper
from django.views.generic.base import TemplateView
from frontend.forms import NewCarForm
from django.shortcuts import render


class NewCarView(TemplateView):
    """
    Class that handles the new car frontend view
    GET - Returns default template
    POST - Sends new car data to create an car
    """
    template_name = APP_TEMPLATE_DIR + "new-car.html"

    def get_context_data(self, **kwargs):
        """
        Override the get_context_data method to add new data to the
        context dictionary that is passed to the template
        """
        context = super().get_context_data(**kwargs)
        return context

    def post(self, request, **kwargs):
        """
        Handles any incoming post requests pointing to this view specifically
        for creating a new car
        """
        context = self.get_context_data()
        form = NewCarForm(self.request.POST)

        if form.is_valid():
            form.cleaned_data['user_id'] = request.user.id
            response = APIHelper.post_to_api('cars/',
                                  self.request.user.auth_token,
                                  form.cleaned_data)
            print(response)
            context['message'] = 'Thank you! Your car has been saved.'
            return render(request, self.template_name, context)
        else:
            context['message'] = 'There was an error with your request.'
            return render(request, self.template_name, context)
