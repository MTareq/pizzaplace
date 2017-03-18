from rest_framework import serializers
from .models import Order, Pizza, Customer


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order

class PizzaSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Pizza
