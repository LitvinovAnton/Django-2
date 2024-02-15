from django.db import models

# Create your models here.
class Client(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    address = models.TextField()
    registration_date = models.DateField(auto_now_add=True)


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()
    added_date = models.DateField(auto_now_add=True)
    # photo = models.ImageField(upload_to='product_photos/',
    #                           default='default_product.jpg')
    # photo = models.ImageField(upload_to='homework_app/product_photos/', null=True, blank=True)
    photo = models.ImageField(upload_to='homework_app/product_photos/', null=True, blank=True,
                              default='homework_app/product_photos/default_image.jpg')


class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    order_date = models.DateField(auto_now_add=False)
