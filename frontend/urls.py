from django.urls import path
from django.contrib.auth import views as auth_views
from .views import HomeView
from .views import LoginView
from .views import RegisterView
from .views import NewCarView
from .views import CarView

app_name = 'frontend'
urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('login', LoginView.as_view(), name="login"),
    path('register', RegisterView.as_view(), name="register"),
    path('new-car', NewCarView.as_view(), name="new-car"),
    path('car/<id>', CarView.as_view(), name="car"),
    path('login2', auth_views.LoginView.as_view(template_name='frontend/login.html'), name="login2")
]
