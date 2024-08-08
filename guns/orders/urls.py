from django.urls import path

from .views import *

urlpatterns = [
    path('order/', OrderCreateView.as_view(), name='order-create'),
    path('order/<int:pk>/', OrderDetailView.as_view(), name='order-detail'),
    path('order/all/', AllOrdersListView.as_view(), name='all-order-list'),
    path('order/delete/<int:pk>/', OrderDeleteView.as_view(), name='order-delete'),
    path('order/update/<int:pk>/', OrderUpdateView.as_view(), name='order-update'),
]