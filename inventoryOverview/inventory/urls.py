from django.urls import path
from . import views


urlpatterns = [
    path('', views.search),
    path('search', views.search, name='order-search'),
    path('result', views.result, name='order-result'),
    path('order/<int:id>', views.order, name='order-detail')
]
