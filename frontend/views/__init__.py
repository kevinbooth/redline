from .car_view import CarView
from .error_404_view import Error404View
from .home_view import HomeView
from .login_view import LoginView
from .new_car_view import NewCarView
from .register_view import RegisterView

APP_TEMPLATE_DIR = 'frontend/'
API_ROOT_URL = 'http://localhost:8000/api/v1/'

__all__ = [
    'CarView',
    'Error404View',
    'HomeView',
    'LoginView',
    'NewCarView',
    'RegisterView'
]
