from django.shortcuts import render

from .models import Coil, Order, OrderItem

def place_order(request):
    coils = Coil.objects.all()
    if request.method == "POST":
        customer_name = request.POST['customer_name']
        order = Order.objects.create(customer_name=customer_name, total_cost=0)

        total_cost = 0
        for item_data in request.POST.getlist('items'):
            item_data = item_data.split(',')  (coil_id, quantity)
            coil_id = int(item_data[0])
            quantity = int(item_data[1])
            coil = Coil.objects.get(id=coil_id)

           
            total_cost += coil.price * quantity

            OrderItem.objects.create(order=order, coil=coil, quantity=quantity)

        order.total_cost = total_cost
        order.save()

        return redirect('view_orders') 
    else:
        return render(request, 'sales/order.html', {'coils': coils})

def view_order(request):
    orders = Order.objects.all()
    return render(request, 'sales/ordersview.html', {'orders': orders})
