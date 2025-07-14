from django.urls import path
from .views import greeting_page

urlpatterns = [
    path('', greeting_page, name='greeting_page'),
]
