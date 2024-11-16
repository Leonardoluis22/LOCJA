from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from .models import Equipamento
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

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
