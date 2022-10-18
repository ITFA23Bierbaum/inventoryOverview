from django.contrib import messages
from django.shortcuts import render
from django.db.models import Q
from .models import Order, InventoryItem, OrderItem


# Create your views here.
def search(request):
    orders = Order.objects.filter()
    return render(request, 'inventory/search.html', {'title': 'Auftrag suchen', 'orders': orders, 'logo': 'ressources/logo.png'})

def order(request):
    orderId= request.POST['selectedOrderId']
    print(orderId)
    current_order = Order.objects.get(id=orderId)
    current_items = OrderItem.objects.filter(order=current_order)
    return render(request, 'inventory/order.html', {'order': current_order, 'items': current_items, 'logo': 'ressources/logo.png'})
