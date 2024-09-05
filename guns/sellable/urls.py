import django.http
from django.urls import path

from .views import *

urlpatterns = [

    #path('', SellableListCreateView.as_view(), name='sellable-list-create'),
    path('<int:_id>/', sellable_list_create_view, name='sellable-list-create'),
    path('<int:_id>/', sellable_detail_view, name='sellable-detail'),
    path('all/', all_sellable_list_view, name='all-sellable-list'),
    path('delete/<int:_id>/', sellable_delete_view, name='sellable-delete'),
    path('update/<int:_id>/', sellable_update_view, name='sellable-update'),
]