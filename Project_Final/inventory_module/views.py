from django.shortcuts import render
from django.utils import timezone
from .models import Inventory
from django.shortcuts import render, get_object_or_404

def inventory_list(request):
    posts = Inventory.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'inventory_module/inventory_list.html', {'Inventory': inventory_list})

def inventory_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})