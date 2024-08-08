from django.shortcuts import render

# Create your views here.

from rest_framework import generics
from rest_framework.settings import api_settings

from .models import Order
from .serializer import OrderSerializer

from rest_framework import status
from rest_framework.response import Response
from sellable.service import Sellable_service


class OrderCreateView(generics.CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    sellable_service = Sellable_service

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        sellable_id = serializer.validated_data['sellable_id']
        contacts = serializer.validated_data['contacts']
        total_price = serializer.validated_data['total_price']
        order = Order.objects.create(sellable_id=sellable_id, contacts=contacts, total_price=total_price)
        print(order)
        self.sellable_service.mark_sellable_as_reserved(self, order.sellable_id)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        serializer.save()

    def get_success_headers(self, data):
        try:
            return {'Location': str(data[api_settings.URL_FIELD_NAME])}
        except (TypeError, KeyError):
            return {}


class OrderListCreateView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class AllOrdersListView(generics.ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    partial = True


class OrderDeleteView(generics.DestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response(print("delete Order"))