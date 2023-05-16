from django.urls import path
from .views import Signup, Login

urlpatterns = [
    path("signup/", Signup, name="signup"), # http://localhost:8000/account/signup/
    path("login/", Login, name="login"), # http://localhost:8000/account/login/
]