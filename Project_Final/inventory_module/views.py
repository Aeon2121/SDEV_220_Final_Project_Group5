from django.shortcuts import render, get_object_or_404
from .models import Inventory

def inventory_list(request):
    items = Inventory.objects.all().order_by('id') 
    return render(request, 'inventory_module/inventory_list.html', {'items': items})

def inventory_detail(request, pk):
    item = get_object_or_404(Inventory, pk=pk)
    return render(request, 'inventory_module/inventory_detail.html', {'item': item})
