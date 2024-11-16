from .models import Fornecedor
from django.views.generic import ListView, CreateView
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