from django.urls import path
from .views import CustomerListView, CustomerCreateView, CustomerDeleteView, CustomerUpdateView

urlpatterns = [
    path("", CustomerListView.as_view(), name='customers_list'),
    path('register/', CustomerCreateView.as_view(), name='customers_register'),
    path("delete/<int:pk>/", CustomerDeleteView.as_view(), name="customers_delete"),
    path("update/<int:pk>/", CustomerUpdateView.as_view(), name="customers_update"),
]