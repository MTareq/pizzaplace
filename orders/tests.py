from django.test import TestCase
from django.core.management import call_command
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from orders.models import Pizza, Order, Customer


class PizzaTestCase(TestCase):

    def setUp(self):
        call_command("loaddata", "pizza.json", verbosity=0)

    def test_pizza_initial_data(self):
        fun_guy_pizza = Pizza.objects.get(id=6)
        self.assertEqual(fun_guy_pizza.name, 'Funghi')

class OrdersAPITest(APITestCase):

    def setUp(self):
        call_command("loaddata", "pizza.json", verbosity=0)
        self.list_url = reverse('order-list')
        self.detail_url = reverse('order-detail', args=[1])
        data = {'pizza_id': 1,
                'pizza_size': 35,
                'customer_name': "Mohammed Ahmed Tareq",
                'customer_address': "#14 Jacoub St."}
        self.creation_response = self.client.post(self.list_url, data, format='json')
        self.customer_details_url = self.creation_response.data['customer']

    def test_order_creation(self):
        self.assertEqual(self.creation_response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Order.objects.count(), 1)
        self.assertEqual(Order.objects.get().pizza.name, "Margherita")
        self.assertEqual(Order.objects.get().pizza_size, 35)
        self.assertEqual(Customer.objects.get().name, "Mohammed Ahmed Tareq")
        self.assertEqual(Customer.objects.get().address, "#14 Jacoub St.")

    def test_order_retrieval(self):
        response = self.client.get(self.detail_url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_order_update(self):
        data = {'pizza_id': 4,
                'pizza_size': 50,
                'customer_name': "Mohammed Ahmed Tareq",
                'customer_address': "#14 Jacoub St."}
        response = self.client.put(self.detail_url, data, format='json')
        self.assertEqual(Order.objects.get().pizza.name, "Napolitana")
        self.assertEqual(Order.objects.get().pizza_size, 50)

    def test_order_partial_update(self):
        data = {'pizza_id': 3,
                'pizza_size': 35}
        response = self.client.patch(self.detail_url, data, format='json')
        self.assertEqual(Order.objects.get().pizza.name, "Hawaiian pizza")
        self.assertEqual(Order.objects.get().pizza_size, 35)

    def test_order_invalid_update(self):
        data = {'pizza_id': 100,
                'pizza_size': 40}
        response = self.client.patch(self.detail_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Order.objects.get().pizza.name, "Margherita")
        self.assertEqual(Order.objects.get().pizza_size, 35)


    def test_order_delete(self):
        response = self.client.delete(self.detail_url, format='json')
        self.assertEqual(Order.objects.count(), 0)
        with self.assertRaises(Order.DoesNotExist):
            Order.objects.get(pk=1)

    def test_customer_details(self):
        response = self.client.get(self.customer_details_url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['orders'][0]['customer_name'], "Mohammed Ahmed Tareq")
        self.assertEqual(response.data['orders'][0]['customer_address'], "#14 Jacoub St.")
        self.assertEqual(response.data['orders'][0]['pizza_id'], 1)
        self.assertEqual(response.data['orders'][0]['pizza_size'], 35)
