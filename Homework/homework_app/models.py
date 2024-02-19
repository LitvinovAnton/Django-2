from django.db import models

# Create your models here.
class Client(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя')
    email = models.EmailField(verbose_name='почта')
    phone_number = models.CharField(max_length=20, verbose_name='телефон')
    address = models.TextField(verbose_name='Адрес')
    registration_date = models.DateField(auto_now_add=True, verbose_name='Дата регистрации')

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='название')
    description = models.TextField(verbose_name='Описание')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    quantity = models.IntegerField(verbose_name='Количество')
    added_date = models.DateField(auto_now_add=True, verbose_name='Дата добавления')
    # photo = models.ImageField(upload_to='product_photos/',
    #                           default='default_product.jpg')
    # photo = models.ImageField(upload_to='homework_app/product_photos/', null=True, blank=True)
    photo = models.ImageField(upload_to='homework_app/product_photos/', null=True, blank=True,
                              default='homework_app/product_photos/default_image.jpg')

    def __str__(self):
        return f'{self.name}'


class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, verbose_name='Клиент')
    products = models.ManyToManyField(Product, verbose_name='Товары')
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Стоимость')
    order_date = models.DateField(auto_now_add=False, verbose_name='Количество')

    def __str__(self):
        return f'{self.client}'
