from django.urls import path
from .views import home

urlpatterns = [
    path('', home.as_view(), name='homepage')
]
