from django.urls import path
from .views import calculate_weight

urlpatterns = [
    path('calculate/', calculate_weight, name='calculate_weight'),
]