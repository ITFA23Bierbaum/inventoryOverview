from django.urls import path
from . import views


urlpatterns = [
    path('', views.search),
    path('search', views.search, name='order-search'),
    path('order', views.order, name='order-detail')
]
