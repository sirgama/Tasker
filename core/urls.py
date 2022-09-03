from django.urls import path
from .views import home, Register

urlpatterns = [
    path('', home.as_view(), name='homepage'),
    path('register/', Register.as_view(), name='signup'),
]
