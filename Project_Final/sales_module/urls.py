from django.urls import path
from . import views

urlpatterns = [
    path('order', views.Orders, name='order'),
    path('ordersview/', views.ordersview, name='ordersview'),
]