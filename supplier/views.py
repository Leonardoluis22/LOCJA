from .models import Fornecedor
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
# Create your views here.
class SupplierListView(ListView):
    template_name = 'supplier/supplier_list.html'
    context_object_name = 'suppliers'
    model = Fornecedor
    login_url = 'login'

class SupplierCreateView(CreateView):
    template_name = "supplier/supplier_register.html"
    model = Fornecedor
    fields = '__all__'
    login_url = 'login'
    success_url = reverse_lazy('supplier_list')

class SupplierUpdateView(LoginRequiredMixin , UpdateView):
    model = Fornecedor
    fields = "__all__"
    template_name = "supplier/supplier_update.html"
    success_url = reverse_lazy("supplier_list")
    login_url = "login" ##Redireciona para a página de login caso o usuário não esteja logado



class SupplierDeleteView(LoginRequiredMixin , DeleteView):
    model = Fornecedor
    template_name = "supplier/supplier_delete.html"
    success_url = reverse_lazy("supplier_list")
    login_url = "login" ##Redireciona para a página de login caso o usuário não esteja logado