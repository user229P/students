from django.urls import path
from .views import *

urlpatterns = [
    path("login", user_login, name="loginUser"),
    path("signup", user_register, name="signupUser"),
    path("logout", user_logout, name="logout"),
    path("update_profile", update_profile, name="update_profile"),
    path("login-failled", login_failled, name="login-failled"),
    path("profile", profile, name="profile"),
]