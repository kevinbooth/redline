"""
Module to define urlpatterns
"""
from django.urls import path, include


urlpatterns = [
    path('user/', include('account.urls')),
    path('cars/', CarView.as_view(), name="cars"),
    path('car/<id>', CarObjectView.as_view(), name="car"),
    path('parts/', PartView.as_view(), name="parts"),
    path('part/<id>', PartObjectView.as_view(), name="part")
]
