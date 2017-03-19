from django.shortcuts import render
from rest_framework import viewsets
from .models import Order, Customer
from .serializers import OrderSerializer, CustomerSerializer


class OrderViewSet(viewsets.ModelViewSet):

    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class CustomerViewSet(viewsets.ModelViewSet):

    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
