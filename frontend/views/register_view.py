from frontend.constants import APP_TEMPLATE_DIR, API_ROOT_URL
from frontend.views.api_helper import APIHelper
from django.views.generic.base import TemplateView
from django.shortcuts import render
from frontend.forms import RegisterForm


class RegisterView(TemplateView):
    """
    Class that handles the register frontend view
    GET - Returns default template
    POST - Inputs user registration data to create an account
    """

    template_name = APP_TEMPLATE_DIR + "register.html"

    def get(self, request):
        """
        Method to returns register template
        """
        return render(request, self.template_name)

    def post(self, request):
        """
        Method to input user registration data to create an account
        """
        message = {}
        form = RegisterForm(self.request.POST)

        if form.is_valid():
            password = form.cleaned_data.get('password')
            confirmed_password = form.cleaned_data.get('confirmed_password')
            if password != confirmed_password:
                message = {'msg': 'Your two passwords did not match. ' +
                           'Please re-register your account.'}
            else:
                del form.cleaned_data['confirmed_password']
                data = form.cleaned_data
                response = APIHelper.public_post_to_api('user/register/', data)
                if response != 200:
                    message = {'msg': 'Username is already taken. ' +
                               'Please re-register your account.'}
                else:
                    data = {'username': form.cleaned_data.get('username'),
                            'password': form.cleaned_data.get('password')}
                    # Create an API auth token for the new user
                    response = APIHelper.public_post_to_api('user/auth/', data)

                    message = {'msg': 'Thank you for registering! ' +
                               'Please login with your new account.'}
                    self.template_name = APP_TEMPLATE_DIR + "login.html"
        else:
            message = {'msg': 'Something went wrong. ' +
                       'Please re-register your account.'}
            return render(request, self.template_name, message)
        return render(request, self.template_name, message)
