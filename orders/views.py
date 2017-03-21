from django.shortcuts import render
from rest_framework import viewsets, mixins
from .models import Order, Customer
from .serializers import OrderSerializer, CustomerSerializer


class OrderViewSet(viewsets.ModelViewSet):

    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class CustomerViewSet(mixins.RetrieveModelMixin,
                      viewsets.GenericViewSet):
    """
        View Set is Limited to retrieve only
    """

    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
