from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.views.generic import DeleteView
from django.views.generic.edit import UpdateView

from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Equipamento
# Create your views here.
class EquipmentListView(LoginRequiredMixin, ListView):
    template_name = 'equipment/equipment_list.html'
    context_object_name = 'equipments'
    model = Equipamento
    login_url = "login"

class EquipmentCreateView(LoginRequiredMixin, CreateView):
    model = Equipamento
    fields = "__all__"
    template_name = "equipment/equipment_register.html"
    success_url = reverse_lazy("equipment_list")
    login_url = "login"

class EquipmentUpdateView(LoginRequiredMixin, UpdateView):
    model = Equipamento
    fields = "__all__"
    template_name = "equipment/equipment_update.html"
    success_url = reverse_lazy("equipment_list")
    login_url = "login"

class EquipmentDeleteView(LoginRequiredMixin , DeleteView):
    model = Equipamento
    template_name = "equipment/equipment_delete.html"
    success_url = reverse_lazy("equipment_list")
    login_url = "login" ##Redireciona para a página de login caso o usuário não esteja logado