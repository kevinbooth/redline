"""
Module to define urlpatterns
"""
from django.urls import path, include


urlpatterns = [
    path('user/', include('account.urls')),
    path('cars/', CarView.as_view(), name="cars"),
    path('car/<id>', CarObjectView.as_view(), name="car"),
    path('tasks/', TaskView.as_view(), name="tasks"),
    path('task/<id>', TaskObjectView.as_view(), name="task")
]
