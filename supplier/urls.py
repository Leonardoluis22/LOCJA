from django.urls import path
from .views import SupplierListView, SupplierCreateView, SupplierUpdateView, SupplierDeleteView

urlpatterns = [
    path("",SupplierListView.as_view(), name="supplier_list"),
    path("register/", SupplierCreateView.as_view(), name="supplier_register"),
    path("update/<int:pk>", SupplierUpdateView.as_view(), name="supplier_update"),
    path("delete/<int:pk>", SupplierDeleteView.as_view(), name="supplier_delete")
]
