from django.urls import path
from .views import SupplierListView, SupplierCreateView

urlpatterns = [
    path("",SupplierListView.as_view(), name="supplier_list"),
    path("register/", SupplierCreateView.as_view(), name="supplier_register")
]
