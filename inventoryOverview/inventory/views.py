import sys

from django.contrib import messages
from django.shortcuts import render
from django.db.models import Q
from .models import Order, InventoryItem, OrderItem, Customer


# Create your views here.
def search(request):
    orders = Order.objects.filter()
    filter_order_no = ''
    filter_customer = ''
    if request.POST.get('orderNoSearch', ''):
        filter_order_no = request.POST.get('orderNoSearch', '')
        print('filter_order_no: ' + filter_order_no)
        if filter_order_no:
            orders = orders.filter(number__startswith=filter_order_no)
    if request.POST['customerSearch']:
        filter_customer = request.POST['customerSearch', '']
        print('filter_customer: ' + filter_customer)
        if filter_customer:
            orders = orders.filter(customer__name__startswith=filter_customer)
    return render(request, 'inventory/orderList.html', {'title': 'Auftrag suchen',
                                                        'orders': orders,
                                                        'filter_order_no': '',
                                                        'filter_customer': ''})


def order(request):
    order_id = request.POST['selectedOrderId']
    current_order = Order.objects.get(id=order_id)
    current_items = OrderItem.objects.filter(order=current_order)
    return render(request, 'inventory/orderDetails.html',
                  {'title': current_order.number + ' - ' + current_order.customer.name,
                   'order': current_order, 'items': current_items})
