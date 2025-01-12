from django.urls import path
from .views import EquipmentListView, EquipmentCreateView, EquipmentDeleteView, EquipmentUpdateView

urlpatterns = [
    path("", EquipmentListView.as_view(), name='equipment_list'),
    path('register/', EquipmentCreateView.as_view(), name='equipment_register'),
    path("delete/<int:pk>/", EquipmentDeleteView.as_view(), name="equipment_delete"),
    path('update/<int:pk>/', EquipmentUpdateView.as_view(), name="equipment_update")
]
