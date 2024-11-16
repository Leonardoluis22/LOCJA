from django.urls import path
from .views import EquipmentListView, EquipmentCreateView

urlpatterns = [
    path("", EquipmentListView.as_view(), name='equipment_list'),
    path('register/', EquipmentCreateView.as_view(), name='equipment_register'),
]
