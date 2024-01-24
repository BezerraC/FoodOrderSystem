from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from .models import (DinnerPlatters, Pasta, RegularPizza, Salad, SicilianPizza,
                     Sub, Toppings, UserOrder)


class ordersTestCase(TestCase):
    def setUp(self):
        # Creating an example user for authentication
        self.user = User.objects.create_user(username='testuser', password='testpass')

    def test_index_view_authenticated(self):
        # Testing whether the view index redirects correctly when the user is authenticated
        self.client.login(username='testuser', password='testpass')
        response = self.client.get(reverse('orders:index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'orders/home.html')

    def test_index_view_unauthenticated(self):
        # Testing whether the view index redirects correctly when the user is not authenticated
        response = self.client.get(reverse('orders:index'))
        self.assertRedirects(response, reverse('orders:login'))

    def test_checkout_view_post_request(self):
        # Testing the checkout view for a POST request
        self.client.login(username='testuser', password='testpass')
        response = self.client.post(reverse('orders:checkout'), {
            'cart': '[{"item_description": "Pizza", "quantity": 2}]',
            'price_of_cart': '20.00',
            'table': '1'
        })
        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(response.content, {'result': 'Pedido Recebido!'})

    def test_checkout_view_get_request(self):
        # Testing the checkout view for a GET request
        response = self.client.get(reverse('orders:checkout'))
        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(response.content, {"nothing to see": "this isn't happening"})

    def test_pizza_view_authenticated(self):
        # Testing the pie view for an authenticated user
        self.client.login(username='testuser', password='testpass')
        response = self.client.get(reverse('orders:pizza'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'orders/pizza.html')

    def test_pizza_view_unauthenticated(self):
        # Testing the pizza view for an unauthenticated user
        response = self.client.get(reverse('orders:pizza'))
        self.assertRedirects(response, reverse('orders:login'))

    def test_pasta_view_authenticated(self):
        # Testing the folder view for an authenticated user
        self.client.login(username='testuser', password='testpass')
        response = self.client.get(reverse('orders:pasta'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'orders/pasta.html')

    def test_pasta_view_unauthenticated(self):
        # Testing folder view for an unauthenticated user
        response = self.client.get(reverse('orders:pasta'))
        self.assertRedirects(response, reverse('orders:login'))

    def test_user_order_model_str_method(self):
        # Testing the model's __str__ method UserOrder
        order = UserOrder(username='testuser', order='Pizza, Pasta', price=15.00, table='1', delivered=False)
        self.assertEqual(str(order), f"Order placed by  : testuser on {order.time_of_order.date()} at {order.time_of_order.time().strftime('%H:%M:%S')}")

    def test_toppings_model_str_method(self):
        # Testing the model's __str__ method Toppings
        topping = Toppings(topping_name='Pepperoni')
        self.assertEqual(str(topping), 'Pepperoni')

    def test_dinner_platters_model_str_method(self):
        # Testing the model's __str__ method DinnerPlatters
        platter = DinnerPlatters(dish_name='Chicken Alfredo', small_price=12.00, large_price=18.00)
        self.assertEqual(str(platter), 'Platter : Chicken Alfredo')

    def test_pasta_model_str_method(self):
        # Testing the model's __str__ method Pasta
        pasta_dish = Pasta(dish_name='Spaghetti Bolognese', price=10.00)
        self.assertEqual(str(pasta_dish), 'Spaghetti Bolognese')

    def test_regular_pizza_model_str_method(self):
        # Testing the model's __str__ method RegularPizza
        pizza = RegularPizza(pizza_choice='Margherita', small_price=8.00, large_price=12.00)
        self.assertEqual(str(pizza), 'Regular Pizza : Margherita')

    def test_salad_model_str_method(self):
        # Testing the model's __str__ method Salad
        salad_dish = Salad(dish_name='Caesar Salad', price=7.50)
        self.assertEqual(str(salad_dish), 'Salad : Caesar Salad')

    def test_sicilian_pizza_model_str_method(self):
        # Testing the model's __str__ method SicilianPizza
        sicilian_pizza = SicilianPizza(pizza_choice='Pepperoni', small_price=10.00, large_price=15.00)
        self.assertEqual(str(sicilian_pizza), 'Sicilian Pizza : Pepperoni')

    def test_sub_model_str_method(self):
        # Testing the model's __str__ method Sub
        sub_filling = Sub(sub_filling='Meatball', small_price=5.00, large_price=6.50)
        self.assertEqual(str(sub_filling), 'Sub : Meatball')

    def test_toppings_model_str_method(self):
        # Testing the model's __str__ method Toppings
        topping = Toppings(topping_name='Pepperoni')
        self.assertEqual(str(topping), 'Pepperoni')

    def test_user_order_model_str_method(self):
        # Testing the model's __str__ method UserOrder
        order = UserOrder(username='testuser', order='Pizza, Pasta', price=15.00, table='1', delivered=False)
        self.assertEqual(str(order), f"Order placed by  : testuser on {order.time_of_order.date()} at {order.time_of_order.time().strftime('%H:%M:%S')}")
