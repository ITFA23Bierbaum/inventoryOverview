import sys

from django.contrib import messages
from django.shortcuts import render
from django.db.models import Q
from .models import Order, InventoryItem, OrderItem, Customer, Shelf
import numpy as np
from python_tsp.exact import solve_tsp_dynamic_programming
from python_tsp.distances import euclidean_distance_matrix

import json
from django.shortcuts import *
from django.template import RequestContext

# Create your views here.
def search(request):
    orders = Order.objects.filter()
    if request.method == "POST" and request.POST.get('isFilter'):
        if request.POST.get('orderNoSearch', ''):
            filter_order_no = request.POST.get('orderNoSearch', '')
            print('filter_order_no: ' + filter_order_no)
            if filter_order_no:
                orders = orders.filter(number__startswith=filter_order_no)
        if request.POST.get('customerSearch'):
            filter_customer = request.POST['customerSearch', '']
            print('filter_customer: ' + filter_customer)
            if filter_customer:
                orders = orders.filter(customer__name__startswith=filter_customer)
        # return HttpResponse(orders)

    return render(request, 'inventory/orderList.html', {'title': 'Auftrag suchen',
                                                        'orders': orders,
                                                        'filter_order_no': '',
                                                        'filter_customer': ''})


def order(request):
    order_id = request.POST['selectedOrderId']
    current_order = Order.objects.get(id=order_id)
    current_orderitems = OrderItem.objects.filter(order=current_order)
    # find the optimal way between the items
    sources = np.array([[0, 0]])
    for current_orderitem in current_orderitems:
        current_shelf = current_orderitem.inventoryItem.shelf
        sources = np.append(sources, [[current_shelf.row, current_shelf.section]], axis=0)
    distance_matrix = euclidean_distance_matrix(sources)  # find distances between points
    permutation, distance = solve_tsp_dynamic_programming(distance_matrix)  # find shortest way
    print(permutation, distance)
    sorted_orderitems = [x for _, x in sorted(zip(permutation[1::], current_orderitems))]
    return render(request, 'inventory/orderDetails.html',
                  {'title': current_order.number + ' - ' + current_order.customer.name,
                   'order': current_order, 'items': sorted_orderitems, 'way': distance})
