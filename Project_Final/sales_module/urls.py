from django.urls import path
from . import views

urlpatterns = [
    path('order/', views.orders, name='order'),
    path('ordersview/', views.ordersview, name='ordersview'),
]