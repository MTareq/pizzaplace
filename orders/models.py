from django.db import models

class Order(models.Model):

    pizza = models.ForiegnKey(Pizza)
    pizza_size = models.IntegerField()
    customer_name = models.CharField(max_length=30)
    customer_address = models.CharField(max_length=100)


class Pizza(models.Model):

    name = models.CharField(max_length=30)

