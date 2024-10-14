from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.contrib import messages


class LoginView(LoginView):
    template_name = "login/login.html"
    fields = "__all__"
    redirect_authenticated_user = True

    def get_sucess_url(self):
        return reverse_lazy("home")

    def form_invalid(self, form):
        messages.error(self.request, "Usuário ou senha inválidos")
        return self.render_to_response(self.get_context_data(form=form))




