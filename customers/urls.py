from django.urls import path
from .views import CustomerListView, CustomerCreateView

urlpatterns = [
    path("", CustomerListView.as_view(), name='customers_list'),
    path('register/', CustomerCreateView.as_view(), name='customers_register'),  # Corrigida a URL
]