from django.urls import path
from .views import home, index, signup, user_login, user_logout

urlpatterns = [
    path("", index, name="index"),
    path("login/", user_login, name="login"),
    path("signup/", signup, name="signup"),
    path("home/", home, name="home"),
    path("logout/", user_logout, name="logout"),
]
