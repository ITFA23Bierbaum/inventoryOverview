import base64
from io import BytesIO

from .models import Order, InventoryItem, OrderItem, Customer, Shelf
import numpy as np
from python_tsp.exact import solve_tsp_dynamic_programming
from python_tsp.distances import euclidean_distance_matrix
import matplotlib.pyplot as plt
import matplotlib.patches as patches

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
    sorted_orderitems = [x for _, x in sorted(zip(permutation[1::], current_orderitems))]

    x_values = [0]
    y_values = [0]
    for item in sorted_orderitems:
        x_values.append(item.inventoryItem.shelf.row)
        y_values.append(item.inventoryItem.shelf.section)
    way_picture = make_route_image(x_values, y_values)

    return render(request, 'inventory/orderDetails.html',
                  {'title': current_order.number + ' - ' + current_order.customer.name,
                   'order': current_order, 'items': sorted_orderitems, 'way': distance, 'picture': way_picture})


def make_route_image(x_values, y_values):
    x = x_values
    y = y_values
    x.append(0)
    y.append(0)

    fig, ax = plt.subplots()

    # Add the patch to the Axes
    ax.add_patch(patches.Rectangle((0, 0), 0.4, 0.4, linewidth=1, edgecolor='#888', facecolor='none'))
    for i in range(1, 4):
        for j in range(1, 19):
            ax.add_patch(
                patches.Rectangle((i - 0.2, j - 0.2), 0.4, 0.4, linewidth=1, edgecolor='#888', facecolor='none'))

    ax.set_aspect('equal', adjustable='box', anchor='C')
    ax.plot(x, y, linewidth=0.75, color='red')
    ax.set_facecolor('#222')

    ax1 = plt.subplot()
    ax1.set_xticks(range(4))
    ax1.set_xticklabels(range(4))
    ax1.set_yticks(range(19))
    ax1.set_yticklabels(range(19))
    # function to save the plot as base64
    tmpfile = BytesIO()

    plt.axis('off')
    fig.savefig(tmpfile, format='png', facecolor='#222', bbox_inches='tight')
    encoded = base64.b64encode(tmpfile.getvalue()).decode('utf-8')
    return encoded
