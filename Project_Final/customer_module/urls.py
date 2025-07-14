from django.urls import path
from . import views


urlpatterns = [
    path("", views.Order_list, name="Order_list"),
    path("Order/<int:pk>/", views.Order_detail, name="Order_detail"),
    path("Order/new/", views.Order_new, name="Order_new"),
    path("Order/<int:pk>/edit/", views.Order_edit, name="Order_edit"),
]
