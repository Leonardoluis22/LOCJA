from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.views.generic.detail import DetailView

from .models import Customer
from django.contrib.auth.mixins import LoginRequiredMixin #Valida se usuário está logado
from django.urls import reverse_lazy


