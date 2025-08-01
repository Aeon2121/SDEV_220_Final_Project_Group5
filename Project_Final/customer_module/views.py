from django.utils import timezone
from .models import Order
from django.shortcuts import render, get_object_or_404
from .forms import OrderForm
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

from sales_module import OrderSys1


def Order_list(request):
    Orders = Order.objects.filter(Order_date__lte=timezone.now()).order_by("Order_date")
    return render(request, "customer_module/Order_list.html", {"Orders": Orders})

@login_required
def Order_detail(request, pk):
    Order = get_object_or_404(request, pk=pk)
    return render(request, "customer_module/Order_detail.html", {"Order": Order})

@login_required
def Order_new(request):
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            OrderSys1.take_order()
            order.Customer = request.user
            order.Order_date = timezone.now()
            order.save()
            return redirect("Order_detail", pk=order.pk)
    else:
        form = OrderForm()
    return render(request, "customer_module/Order_edit.html", {"form": form})

