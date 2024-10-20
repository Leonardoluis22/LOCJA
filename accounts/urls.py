from django.urls import path, include
from accounts.views import LoginView
from django.contrib.auth.views import LogoutView
from .views import SignUpView

urlpatterns = [
    path("login/", LoginView.as_view(), name="login"),
    path("accounts/", include("django.contrib.auth.urls")),
    path("signup/", SignUpView.as_view(), name="signup"),
]
