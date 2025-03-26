from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView, TemplateView
from accounts.views import SignUpView
from django.contrib.auth.views import LogoutView
# from customers.views import CustomerListView, CustomerCreateView

urlpatterns = [
    path("admin/", admin.site.urls, name="admin"),
    path("accounts/", include("accounts.urls")),
    path("/", include('home.urls')),
    path("", RedirectView.as_view(url="/accounts/login"), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("signup/", SignUpView.as_view(), name="signup"),
    path("customers/", include("customers.urls")), 
    path("supplier/", include("supplier.urls")),
    path("equipment/", include("equipment.urls")),
    # path("aluguel/", include("aluguel.urls")),
    
]
