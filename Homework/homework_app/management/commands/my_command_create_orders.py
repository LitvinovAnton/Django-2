import datetime

from django.core.management.base import BaseCommand
from homework_app.models import Client, Product, Order
from faker import Faker

# from Homework.homework_app.models import Product

fake = Faker()


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
            self.create_orders()

    @staticmethod
    def create_orders():
        clients = Client.objects.all()
        products = Product.objects.all()

        for client in clients:
            for _ in range(fake.random_int(min=10, max=20)):
                current_date = datetime.datetime.now()
                start_date = current_date - datetime.timedelta(days=365)
                fake_date = fake.date_time_between(start_date=start_date, end_date=current_date)
                order = Order(
                    client=client,
                    total_amount=0,
                    order_date=fake_date,
                )
                order.save()

                order_products = []

                for _ in range(fake.random_int(min=5, max=10)):
                    product = fake.random_element(products)
                    order_products.append(product)
                    order.total_amount += product.price

                order.products.set(order_products)
                order.save()

    # @staticmethod
    # def create_orders():
    #     clients = Client.objects.all()
    #     products = Product.objects.all()
    #
    #
    #     for client in clients:
    #         current_date = datetime.datetime.now()
    #         order = Order(
    #             client=client,
    #             total_amount=0,
    #             order_date=fake.date_between(start_date='-365d', end_date=current_date),
    #         )
    #         order.save()
    #
    #         order_products = []
    #
    #         for _ in range(fake.random_int(min=5, max=10)):
    #             product = fake.random_element(products)
    #             order_products.append(product)
    #             order.total_amount += product.price
    #
    #         order.products.set(order_products)
    #         order.save()