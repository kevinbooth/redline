"""
frontend/views/edit_car_view.py
Author: Kevin Booth
Last Updated: 5/1/2019
"""
from frontend.constants import APP_TEMPLATE_DIR, API_ROOT_URL
from frontend.views.api_helper import APIHelper
from django.views.generic.base import TemplateView
from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from frontend.forms import NewCarForm


class EditCarView(TemplateView):
    """
    Class that handles the edit car frontend view
    GET - Returns default template
    POST - Sends edited car data to edit a car or delete a car
    """
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

    def post(self, request, id, **kwargs):
        """
        Handles any incoming post requests pointing to this view specifically
        for editing a car and deleting a car
        """
        if request.POST.get("delete"):
            response = APIHelper.delete_from_api('car/' + id,
                                                 self.request.user.auth_token)
            self.template_name = APP_TEMPLATE_DIR + "home.html"
            return HttpResponseRedirect(reverse('home', kwargs={'version': 'v1'}))
        else:
            print("in else")
            return render(request, self.template_name)
