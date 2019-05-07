"""
Module that renders the login page
frontend/views/login_view.py
Author: Kevin Booth
Last Updated: 5/1/2019
"""
from frontend.constants import APP_TEMPLATE_DIR, API_ROOT_URL
from django.views.generic.base import TemplateView


class LoginView(TemplateView):
    """
    Class that handles the login frontend view
    GET - Returns default template
    """
    template_name = APP_TEMPLATE_DIR + "login.html"

    def get_context_data(self, **kwargs):
        """
        Override the get_context_data method to add new data to the
        context dictionary that is passed to the template
        """
        context = super().get_context_data(**kwargs)
        return context
