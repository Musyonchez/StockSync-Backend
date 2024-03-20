from django.urls import path
from . import views

urlpatterns = [
    path('notifications/', views.notifications, name='notifications'),
    
    path('products/', views.product_list, name='products'),

    path('test/', views.test, name='test'),

]
