from django.shortcuts import render

# Create your views here.
def dashboard_view(request):
    # Dashboard
    context = {
        'data': 'Aqui vai a lógica do dashboard'
    }
    return render(request, 'home/dashboard.html', context)