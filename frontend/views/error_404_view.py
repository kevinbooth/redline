"""
frontend/views/error_404_view.py
Author: Kevin Booth
Last Updated: 5/1/2019
"""
from frontend.constants import APP_TEMPLATE_DIR, API_ROOT_URL
# import requests
from django.views.generic.base import TemplateView


class Error404View(TemplateView):
    """
    Class that handles the error 404 frontend view
    GET - Returns default template
    """
    template_name = APP_TEMPLATE_DIR + "404.html"

    def get_context_data(self, **kwargs):
        """
        Override the get_context_data method to add new data to the
        context dictionary that is passed to the template
        """
        context = super().get_context_data(**kwargs)
        return context
