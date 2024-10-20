from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.contrib import messages
from django.views.generic import CreateView


class LoginView(LoginView):
    template_name = "registration/login.html"
    ##fields = "__all__"
    redirect_authenticated_user = True

    def get_sucess_url(self):
            return reverse_lazy("home")

    def form_invalid(self, form):
        messages.error(self.request, "Usuário ou senha inválidos")
        return super().form_invalid(form)


## Classe para criar um novo usuário

class SignUpView(CreateView):
     form_class = UserCreationForm
     success_url = reverse_lazy("login")
     template_name = "registration/signup.html"
     






