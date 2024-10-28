from django.urls import path
from .views import CustomerListView


urlpatterns = [
    path('customers/', CustomerListView.as_views(), name='customers_list'),
]