from django.urls import path
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LogoutView
from .views import HomeView, CarView
from .views import LoginView, RegisterView
from .views import NewCarView, NewTaskView

app_name = 'frontend'

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path(
            'login/',
            auth_views.LoginView.as_view(template_name='frontend/login.html'),
            name="login"
        ),
    path('logout/', LogoutView.as_view(), name="logout"),
    path('register/', RegisterView.as_view(), name="register"),
    path('new-car/', NewCarView.as_view(), name="new-car"),
    path('car/<id>/', CarView.as_view(), name="car"),
    path('car/<id>/new-task/', NewTaskView.as_view(), name="car"),
]
