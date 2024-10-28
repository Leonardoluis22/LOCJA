from django.views.generic.list import ListView
from .models import Customer
from django.contrib.auth.mixins import LoginRequiredMixin ##Valida se usuário está logado

class CustomerListView(LoginRequiredMixin ,ListView):
    model = Customer
    paginate_by = 10


    template_name = "customers/customers_list.html"
    context_object_name = "customers"
    login_url = "login" ##Redireciona para a página de login caso o usuário não esteja logado
