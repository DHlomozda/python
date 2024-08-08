from django.shortcuts import render

# Create your views here.

from rest_framework import generics
from .models import Sellable
from .serializer import SellableSerializer
from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework import status
from rest_framework.response import Response

class JsonView(APIView):
    def get(self, request):
        return Response({'some': 'data'})



class SellableListCreateView(generics.ListCreateAPIView):
    queryset = Sellable.objects.all()
    serializer_class = SellableSerializer


class SellableDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Sellable.objects.all()
    serializer_class = SellableSerializer


class AllSellableListView(generics.ListAPIView):
    queryset = Sellable.objects.all()
    serializer_class = SellableSerializer


class SellableUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Sellable.objects.all()
    serializer_class = SellableSerializer
    partial = True


class SellableDeleteView(generics.DestroyAPIView):
    queryset = Sellable.objects.all()
    serializer_class = SellableSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response(print("delete Movie"))