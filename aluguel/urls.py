from django.urls import path
from .views import AluguelCreateView, AluguelDeleteView, AluguelListView, AluguelUpdateView


urlpatterns = [
    path("", AluguelListView.as_view(), name='aluguel_list'),
    path("register/", AluguelCreateView.as_view(), name='aluguel_register'),
    path("delete/<int:pk>/", AluguelDeleteView.as_view(), name="aluguel_delete"),
    path("update/<int:pk>/", AluguelUpdateView.as_view(), name="aluguel_update"),
]
