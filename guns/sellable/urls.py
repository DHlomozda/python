from django.urls import path

from .views import *

urlpatterns = [

    path('sellable/', SellableListCreateView.as_view(), name='sellable-list-create'),
    path('sellable/<int:pk>/', SellableDetailView.as_view(), name='sellable-detail'),
    #path('sellable/all/', AllSellableListView.as_view(), name='all-sellable-list'),
    path('sellable/delete/<int:pk>/', SellableDeleteView.as_view(), name='sellable-delete'),
    path('sellable/update/<int:pk>/', SellableUpdateView.as_view(), name='sellable-update'),
]