"""
Module to define urlpatterns
"""
from django.urls import path, include
from .views import CarView, CarObjectView


urlpatterns = [
    path('user/', include('account.urls')),
    path('cars/', CarView.as_view(), name="cars"),
    path('car/', CarObjectView.as_view(), name="car")
]
