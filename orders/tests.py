import ipdb
from django.test import TestCase
from django.core.management import call_command
from orders.models import Pizza


class PizzaTestCase(TestCase):

    def test_pizza_initial_data(self):
        call_command("loaddata", "pizza.json", verbosity=0)
        fun_guy_pizza = Pizza.objects.get(id=6)
        self.assertEqual(fun_guy_pizza.name, 'Funghi')

