from django.db import models



class Pizza(models.Model):

    name = models.CharField(max_length=30)


class Customer(models.Model):

    name = models.CharField(max_length=30)
    address = models.CharField(max_length=120)



class Order(models.Model):

    pizza = models.ForeignKey(Pizza)
    pizza_size = models.IntegerField()
    customer_name = models.CharField(max_length=30)
    customer_address = models.CharField(max_length=120)
    customer = models.ForeignKey(Customer, related_name='orders')

