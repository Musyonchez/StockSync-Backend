from django.urls import path
from . import views # Adjust this import if your views are in a different module

urlpatterns = [
    path('lipa_na_mpesa_online/', views.lipa_na_mpesa_online, name='lipa_na_mpesa_online'),
    path('C2B-VALIDATION/', views.c2b_validation, name="c2b-validation"),
    path('C2B-CONFIRMATION/', views.c2b_confirmation, name="c2b-confirmation"),
]
