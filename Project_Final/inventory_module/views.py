from django.shortcuts import render, get_object_or_404, redirect
from .models import Inventory
from .forms import InventoryForm

def inventory_list(request):
    items = Inventory.objects.all().order_by('id') 
    return render(request, 'inventory_module/inventory_list.html', {'items': items})

def inventory_detail(request, pk):
    item = get_object_or_404(Inventory, pk=pk)
    return render(request, 'inventory_module/inventory_detail.html', {'item': item})

def inventory_list(request):
    if request.method == 'POST':
        form = InventoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inventory_list')
    else:
        form = InventoryForm()

    items = Inventory.objects.all().order_by('id')
    return render(request, 'inventory_module/inventory_list.html', {'items': items, 'form': form})