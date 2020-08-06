from django.urls import path
from .views import UserRegistration

urlpatterns = [
    # Adding URL path for user registration page
    path('register/', UserRegistration.as_view(), name="register"),
]