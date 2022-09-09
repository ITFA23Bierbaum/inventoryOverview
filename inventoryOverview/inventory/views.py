from django.contrib import messages
from django.shortcuts import render
from django.db.models import Q
from .models import Order, InventoryItem, OrderItem


# Create your views here.
def search(request):
    return render(request, 'inventory/search.html')


def result(request):
    if request.method == 'POST':
        searched = request.POST['searched']
        if searched != '':
            items = Order.objects.filter(Q(number__contains=searched))
            return render(request, 'inventory/result.html', {'searched': searched, 'items': items})
        else:
            return render(request, 'inventory/result.html', {'searched': searched})
    else:
        return render(request, 'inventory/search.html')


def order(request, id):
    current_order = Order.objects.get(id=id)
    current_items = OrderItem.objects.filter(order=current_order)
    return render(request, 'inventory/order.html', {'order': current_order, 'items': current_items})


