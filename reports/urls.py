from django.urls import path
from . import views

app_name = 'reports'

urlpatterns = [
    path('aluguel/', views.aluguel_report, name='aluguel_report'),
    path('cliente/', views.cliente_report, name='cliente_report'),
    path('equipamento/', views.equipamento_report, name='equipamento_report'),
]
