from django.core.management.base import BaseCommand
from homework_app.models import Client, Product, Order
from faker import Faker

# from Homework.homework_app.models import Product

fake = Faker()


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        self.create_clients()
        self.create_products()
        self.create_orders()

    @staticmethod
    def create_clients():
        for i in range(10):
            client = Client(
                name=fake.name(),
                email=fake.email(),
                phone_number=fake.phone_number(),
                address=fake.city(),
            )
            client.save()

    # @staticmethod
    # def create_products():
    #     for i in range(10):
    #         product = Product(
    #             name=fake.name(),
    #             description=fake.text(),
    #             price=fake.pydecimal(left_digits=5, right_digits=2, positive=True),
    #             quantity=fake.random_int(min=1, max=100),
    #         )
    #         product.save()
    @staticmethod
    def create_products():
        products = ["ручка", "стол", "стул", "карандаш", "книга",
                    "компьютер", "топор", "лампочка", "тетрадь", "стирательная резинка",
                    "маркер", "блокнот", "пила", "шкаф", "пылесос", "тарелка",
                    "бокал", "кастрюля", "перчатки", "колесо"]  # и т.д. добавьте другие предметы в список
        for i in range(10):
            product = Product(
                name=fake.random_element(products),
                description=fake.text(),
                price=fake.pydecimal(left_digits=5, right_digits=2, positive=True),
                quantity=fake.random_int(min=1, max=100),
            )
            product.save()

    @staticmethod
    def create_orders():
        clients = Client.objects.all()
        products = Product.objects.all()

        for client in clients:
            order = Order(
                client=client,
                total_amount=0,
                order_date=fake.date_this_year(),
            )
            order.save()

            order_products = []

            for _ in range(fake.random_int(min=1, max=5)):
                product = fake.random_element(products)
                order_products.append(product)
                order.total_amount += product.price

            order.products.set(order_products)
            order.save()


# class Command(BaseCommand):
#     def handle(self, *args, **kwargs):
#         for i in range(10):
#             client = Client(
#                 name=fake.name(),
#                 email=fake.email(),
#                 phone_number=fake.phone_number(),
#                 address=fake.city(),
#             )
#             client.save()
#
#             product = Product(
#                 name=fake.name(),
#                 description=fake.text(),
#                 price=fake.pydecimal(left_digits=5, right_digits=2, positive=True),
#                 quantity=fake.random_int(min=1, max=100),
#             )
#             product.save()
#
#     @staticmethod
#     def create_orders():
#         clients = Client.objects.all()
#         products = Product.objects.all()
#
#         for client in clients:
#             order = Order(
#                 client=client,
#                 total_amount=0,
#                 order_date=fake.date_this_year(),
#             )
#             order.save()
#
#             order_products = []
#
#             for _ in range(fake.random_int(min=1, max=5)):
#                 product = fake.random_element(products)
#                 order_products.append(product)
#                 order.total_amount += product.price
#
#             order.products.set(order_products)
#             order.save()
