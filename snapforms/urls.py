from django.urls import path
from .views import request_location

urlpatterns = [
    path('request-location-form/', request_location, name='request-location'),
]
