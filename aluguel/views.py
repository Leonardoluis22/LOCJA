from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.views.generic.detail import DetailView

from .models import Aluguel
from django.contrib.auth.mixins import LoginRequiredMixin #Valida se usuário está logado
from django.urls import reverse_lazy

class AluguelCreateView(LoginRequiredMixin, CreateView):
    model = Aluguel
    fields = "__all__"
    template_name = "aluguel/aluguel_register.html"
    success_url = reverse_lazy("aluguel_list")

class AluguelListView(LoginRequiredMixin ,ListView):
    model = Aluguel
    paginate_by = 10
    template_name = "aluguel/aluguel_list.html"
    context_object_name = "alugueis"
    login_url = "login" ##Redireciona para a página de login caso o usuário não esteja logado

class AluguelUpdateView(LoginRequiredMixin , UpdateView):
    model = Aluguel
    fields = "__all__"
    template_name = "aluguel/aluguel_update.html"
    success_url = reverse_lazy("aluguel_list")
    login_url = "login" ##Redireciona para a página de login caso o usuário não esteja logado


class AluguelDeleteView(LoginRequiredMixin , DeleteView):
    model = Aluguel
    template_name = "aluguel/aluguel_delete.html"
    success_url = reverse_lazy("aluguel_list")
    login_url = "login" ##Redireciona para a página de login caso o usuário não esteja logado