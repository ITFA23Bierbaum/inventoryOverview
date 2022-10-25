from django.urls import path
from . import views


urlpatterns = [
    path('', views.search),
    path('orderList', views.search, name='order-search'),
    path('orderDetail', views.order, name='order-detail')
]
