import json

from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render

# Create your views here.

from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.exceptions import NotFound
from rest_framework.renderers import JSONRenderer

from .models import Sellable
from .serializer import SellableSerializer
from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework import status
from rest_framework.response import Response


class JsonView(APIView):
    def get(self, request):
        return Response({'some': 'data'})


# class SellableListCreateView(generics.ListCreateAPIView):
#     queryset = Sellable.objects.all()
#     serializer_class = SellableSerializer

@api_view(['POST'])
def sellable_list_create_view(request, _id):
    new_object = request.body.decode('utf-8')
    body = json.loads(new_object)
    print(f'body: {body}')
    new = Sellable.objects.create(id= _id, category=body.get('category'), title=body.get('title'),
                                  description=body.get('description'), is_Reserved=body.get('is_Reserved'),
                                  photo_Url=body.get('photo_Url'), is_bought=body.get('is_bought')
                                  )
    print(f'new: {new}')
    new.save()
    list_of_sellable = Sellable.objects.all()
    serializer = SellableSerializer(list_of_sellable, many=True)
    print(f'serializer: {serializer}')
    return Response(serializer.data)


@api_view(['GET'])
def sellable_detail_view(request, _id):
    one_object = Sellable.objects.get(pk=_id)
    print(one_object)
    serializer = SellableSerializer(one_object)
    return Response(serializer.data)

# class AllSellableListView(generics.ListAPIView):
#     queryset = Sellable.objects.all()
#     serializer_class = SellableSerializer


@api_view(['GET'])
def all_sellable_list_view(request):
    sellable_list = Sellable.objects.all()
    print(sellable_list)
    serializer = SellableSerializer(sellable_list, many=True)
    return Response(serializer.data)


# class SellableUpdateView(generics.RetrieveUpdateAPIView):
#     queryset = Sellable.objects.all()
#     serializer_class = SellableSerializer
#     partial = True


@api_view(['PUT'])
def sellable_update_view(request, _id):
    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)
    print(f'body: {body}')
    print(f'id: {_id}')
    update_result = Sellable.objects.filter(id=_id).update(category=body.get('category'),
                                                             title=body.get('title'), description=body.get('description'),
                                                             is_Reserved=body.get('is_Reserved'), photo_Url=body.get('photo_Url'),
                                                             is_bought=body.get('is_bought')
                                                             )
    if update_result != 0:
        object = Sellable.objects.get(pk=_id)
        print(object)
        serializer = SellableSerializer(object)
        print(serializer.data)
        return Response(serializer.data)
    return HttpResponseNotFound('Page not found')


class SellableDeleteView(generics.DestroyAPIView):
    queryset = Sellable.objects.all()
    serializer_class = SellableSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response(print("delete Movie"))


@api_view(['DELETE'])
def sellable_delete_view(request, _id):
    print('delete start')
    delete_result = Sellable.objects.get(id=_id)
    print(delete_result)
    delete_result.delete()
    serializer = SellableSerializer(delete_result)
    return Response(serializer.data)