from functools import partial
import json
from django import db
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Order
from .serializers import OrderSerializer


# Create your views here.


class OrderAPIView(APIView):

    def get(self,request):
        id = request.GET.get('id')
        print(id)
        print(request.GET)

        if id:
            print("Entered the individual get request")
            order = get_object_or_404(Order,id=id)
            print(order)
            serialized_order = OrderSerializer(order)
            print(serialized_order)
            return Response(serialized_order.data)
        
        
        #we are fetching all orders 
        orders = Order.objects.all()
        print(orders)
        serialized_orders = OrderSerializer(orders,many= True)
        print(serialized_orders)
        return Response(serialized_orders.data)
    
    def post(self,request):
        data = json.loads(request.body)
        print(data)
        order_Serializer = OrderSerializer(data=data)
        x = order_Serializer.is_valid()
       
        if order_Serializer.is_valid():
            order_Serializer.save()
            return HttpResponse("order saved successfully")
        else:
            print("False")
            print(order_Serializer.errors)
            return HttpResponse("Mine")
    
    def put(self,request):
        data = json.loads(request.body)
        print(data)
        input_id = request.GET.get('id')
        data = json.loads(request.body)
        if input_id :
            db_object = get_object_or_404(Order,id=input_id)
            print(db_object)
            order_serializer = OrderSerializer(db_object,data=data,partial=True)
            if order_serializer.is_valid():
                order_serializer.save()
                return HttpResponse("order updated successfully")
            else:
                print("False")
                print(order_serializer.errors)
                return HttpResponse("Mine")
    
    def delete(self,request):

        input_id = request.GET.get('id')
        if input_id :
            db_object = get_object_or_404(Order,id=input_id)
            print(db_object)
            db_object.delete()
            return HttpResponse("hi how are u")

    

