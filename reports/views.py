from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import AluguelFilterForm, ClienteFilterForm, EquipamentoFilterForm
from .utils import generate_pdf_report

@login_required
def aluguel_report(request):
    form = AluguelFilterForm(request.GET)
    context = {'form': form}
    
    if form.is_valid():
        # Lógica de filtro será implementada aqui
        pass
    
    return render(request, 'reports/aluguel_report.html', context)

@login_required
def cliente_report(request):
    form = ClienteFilterForm(request.GET)
    context = {'form': form}
    
    if form.is_valid():
        # Lógica de filtro será implementada aqui
        pass
    
    return render(request, 'reports/cliente_report.html', context)

@login_required
def equipamento_report(request):
    form = EquipamentoFilterForm(request.GET)
    context = {'form': form}
    
    if form.is_valid():
        # Lógica de filtro será implementada aqui
        pass
    
    return render(request, 'reports/equipamento_report.html', context)
