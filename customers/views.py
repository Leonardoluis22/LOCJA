from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.views.generic.detail import DetailView

from .models import Customer
from django.contrib.auth.mixins import LoginRequiredMixin #Valida se usuário está logado
from django.urls import reverse_lazy


class CustomerCreateView(LoginRequiredMixin , CreateView):
    model = Customer
    fields = "__all__"
    template_name = "customers/customers_register.html"
    success_url = reverse_lazy("customers_list")
    login_url = "login" ##Redireciona para a página de login caso o usuário não esteja logado

class CustomerListView(LoginRequiredMixin ,ListView):
    model = Customer
    paginate_by = 10

    template_name = "customers/customers_list.html"
    context_object_name = "customers"
    login_url = "login" ##Redireciona para a página de login caso o usuário não esteja logado

    # def get(self, request, *args, **kwargs):
    #     request.session['customers'] = "customers"
    #     return super(CustomerListView, self).get(request, *args, **kwargs)

class CustomerUpdateView(LoginRequiredMixin , UpdateView):
    model = Customer
    fields = "__all__"
    template_name = "customers/customers_update.html"
    success_url = reverse_lazy("customers_list")
    login_url = "login" ##Redireciona para a página de login caso o usuário não esteja logado



class CustomerDeleteView(LoginRequiredMixin , DeleteView):
    model = Customer
    template_name = "customers/customers_delete.html"
    success_url = reverse_lazy("customers_list")
    login_url = "login" ##Redireciona para a página de login caso o usuário não esteja logado