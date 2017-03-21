from rest_framework import serializers
from .models import Order, Pizza, Customer


PIZZA_SIZES = ((35, '35 CM'), (50, '50 CM'))

class OrderSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:

        model = Order
        fields = ('id', 'pizza_id', 'pizza', 'pizza_size', 'customer_name', 'customer_address', 'customer', )
        read_only_fields = ('id',)

    customer_name = serializers.CharField(required=True)
    customer_address = serializers.CharField(required=True)
    pizza_size = serializers.ChoiceField(choices=PIZZA_SIZES)
    pizza_id = serializers.IntegerField()
    pizza = serializers.SlugRelatedField(read_only=True, slug_field='name')
    customer = serializers.HyperlinkedRelatedField(view_name='customer-detail', read_only=True)

    def create(self, validated_data):
        
        customer_name = validated_data.get('customer_name')
        customer_address = validated_data.get('customer_address')
        pizza_id = validated_data.pop('pizza_id')
        try:
            pizza = Pizza.objects.get(id=pizza_id)
        except Pizza.DoesNotExist:
            raise serializers.ValidationError("Pizza Does Not Exist")
        customer, created = Customer.objects.get_or_create(name=customer_name, address=customer_address)
        order = Order.objects.create(pizza=pizza, customer=customer, **validated_data)

        return order

    def update(self, instance, validated_data):
        """
            PUT/PATCH Support for full form update or partial Updates

        """
        customer_name = validated_data.get('customer_name', instance.customer_name)
        customer_address = validated_data.get('customer_address', instance.customer_address)
        pizza_id = validated_data.get('pizza_id', instance.pizza.id)
        pizza_size = validated_data.get('pizza_size', instance.pizza_size)
        try:
            pizza = Pizza.objects.get(id=pizza_id)
        except Pizza.DoesNotExist:
            raise serializers.ValidationError("Pizza Does Not Exist")
        customer, created = Customer.objects.get_or_create(name=customer_name, address=customer_address)
        instance.pizza = pizza
        instance.pizza_size = pizza_size
        instance.customer = customer
        instance.customer_name = customer_name
        instance.customer_address = customer_address

        return instance


class CustomerSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:

        model = Customer
        fields = ('name', 'address', 'orders',)
        depth = 1

    orders = OrderSerializer(many=True)

