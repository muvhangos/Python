from django.urls import path
from .views import service_request_list, add_service_request

urlpatterns = [
    path('', service_request_list, name='service_request_list'),
    path('add/', add_service_request, name='add_service_request'),
]