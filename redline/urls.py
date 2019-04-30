"""
Module to define urlpatterns
"""
from django.urls import path, include
from .views import CarView, CarObjectView, TaskView, TaskObjectView
from .views import PartView, PartObjectView

urlpatterns = [
    path('user/', include('account.urls')),
    path('cars/', CarView.as_view(), name="cars"),
    path('car/<id>', CarObjectView.as_view(), name="car"),
    path('car/<id>/tasks/', TaskView.as_view(), name="tasks"),
    path('task/<id>', TaskObjectView.as_view(), name="task"),
    path('parts/', PartView.as_view(), name="parts"),
    path('part/<id>', PartObjectView.as_view(), name="part")
]
