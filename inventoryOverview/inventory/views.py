from django.contrib import messages
from django.shortcuts import render
from django.db.models import Q
from .models import Order, InventoryItem, OrderItem


# Create your views here.
def search(request):
    orders = Order.objects.filter()
    return render(request, 'inventory/orderList.html', {'title': 'Auftrag suchen', 'orders': orders})

def order(request):
    orderId= request.POST['selectedOrderId']
    print(orderId)
    current_order = Order.objects.get(id=orderId)
    current_items = OrderItem.objects.filter(order=current_order)
    return render(request, 'inventory/order.html', {'order': current_order, 'items': current_items})
