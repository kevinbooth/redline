from django.urls import path
from .views import HomeView
from .views import LoginView
from .views import RegisterView
from .views import NewCarView

app_name = 'frontend'
urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('login', LoginView.as_view(), name="login"),
    path('register', RegisterView.as_view(), name="register"),
    path('new-car', NewCarView.as_view(), name="new-car")
]
