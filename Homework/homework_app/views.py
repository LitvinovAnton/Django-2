import datetime
import logging
import random
from collections import defaultdict

from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse, JsonResponse, Http404
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
import pytz

from .form import ProductForm
from .models import Client, Product, Order

# Create your views here.
logger = logging.getLogger(__name__)


def home(request):
    html = """
    <h1>Добро пожаловать на мой первый Django сайт!</h1>
    <p>Это сайт-домашка.</p>
    """
    cur_time = datetime.datetime.now(pytz.timezone('Europe/Moscow')).strftime("%Y-%m-%d %H:%M:%S")
    # current_time = timezone.now().strftime("%Y-%m-%d %H:%M:%S")
    logger.info(f'{cur_time} - homepage')
    return HttpResponse(html)


def about(request):
    # timezone.activate('Europe/Moscow')
    html = """
    <h2>Обо мне</h2>
    <p>Привет, я Бурлаков Валерий, студент GeekBrains, пишу домашку по Django.</p>
    """
    cur_time = datetime.datetime.now(pytz.timezone('Europe/Moscow')).strftime("%Y-%m-%d %H:%M:%S")
    # current_time = timezone.now().strftime("%Y-%m-%d %H:%M:%S")
    logger.info(f'{cur_time} - about us page')
    return HttpResponse(html)


# ===================================CRUD operations=============================================

# ========================================Create===================================================
# операции создания Клиентов, товаров и заказов находятся в файле commands/my_command.py


# ========================================Read===================================================

def get_client(request, client_id):
    client = Client.objects.get(id=client_id)
    # Here, create an HTML table to display the client details
    html = f"""
    <h2>Карточка клиента</h2>
    <table>
        <tr>
            <th>ID клиента</th>
            <th>ФИО</th>
            <th>Email</th>
            <th>Номер телефона</th>
        </tr>
        <tr>
            <td>{client.id}</td>
            <td>{client.name}</td>
            <td>{client.email}</td>
            <td>{client.phone_number}</td>
        </tr>
    </table>
    """
    return HttpResponse(html)


def get_product(request, product_id):
    product = Product.objects.get(id=product_id)
    return render(request, 'homework_app/get_product.html', {'product': product})


def get_order(request, order_id):
    order = Order.objects.get(id=order_id)
    order_products = order.products.all()  # Получаем все заказы по данному заказу
    # Create an HTML table to display the order details
    html = f"""
    <h2>Карточка заказа</h2>
    <table>
        <tr>
            <th>ID заказа</th>
            <th>Клиент</th>
            <th>Полная стоимость</th>
            <th>Дата заказа</th>
        </tr>
        <tr>
            <td>{order.id}</td>
            <td>{order.client.name}</td>
            <td>{order.total_amount}</td>
            <td>{order.order_date}</td>
        </tr>
    </table>
    <h2>Товары в заказе</h2>
    <table>
        <tr>
            <th>ID Товара</th>
            <th>Количество</th>
            <th>стоимость</th>
        </tr>
    """
    for order_product in order_products:
        html += f"""
        <tr>
            <td>{order_product.id}</td>
            <td>{order_product.quantity}</td>
            <td>{order_product.price}</td>
            
        </tr>
        """
    html += "</table>"
    return HttpResponse(html)


def products_by_order(request, order_id):
    order = Order.objects.get(id=order_id)
    order_products = order.products.all()
    context = {
        'order_id': order_id,
        'order_products': order_products
    }
    return render(request, 'homework_app/products_by_order.html', context)


def get_all_clients(request):
    clients = Client.objects.all()
    return render(request, 'homework_app/all_clients.html', {'clients': clients})


def get_all_products(request):
    products = Product.objects.all()
    return render(request, 'homework_app/all_products.html', {'products': products})


def get_all_orders(request):
    orders = Order.objects.all()
    return render(request, 'homework_app/all_orders.html', {'orders': orders})


# ========================================Update===================================================
def update_name_client(request, client_id, update_name):
    try:
        client = Client.objects.get(id=client_id)
        client.name = update_name
        client.save()
        return JsonResponse({'message': 'Имя успешно изменено'})
    except ObjectDoesNotExist:
        return HttpResponse('Отсутствует клиент с таким id', status=404)
    except Exception as e:
        return HttpResponse(f'ОШИБКАСЪ: {str(e)}', status=500)


def update_price_product(request, product_id, updated_price):
    try:
        product = Product.objects.get(id=product_id)
        product.price = updated_price
        product.save()
        return JsonResponse({'message': 'Цена успешно изменена'})
    except ObjectDoesNotExist:
        return HttpResponse('Отсутствует продукт с таким id', status=404)
    except Exception as e:
        return HttpResponse(f'ОШИБКАСЪ: {str(e)}', status=500)


def add_product_to_order(request, order_id, product_id):
    try:
        order = get_object_or_404(Order, id=order_id)
        product = get_object_or_404(Product, id=product_id)
        order.products.add(product)
        order.total_amount += product.price
        order.save()

        return JsonResponse({'message': 'Товар успешно добавлен к заказу'})
    except Http404:
        return HttpResponse('Отсутствует заказ или товар с таким id', status=404)
    except Exception as e:
        return HttpResponse(f'ОШИБКА: {str(e)}', status=500)


def remove_product_from_order(request, order_id, product_id):
    try:
        order = get_object_or_404(Order, id=order_id)
        product = get_object_or_404(Product, id=product_id)

        if product in order.products.all():
            order.products.remove(product)
            order.total_amount -= product.price
            order.save()
            return JsonResponse({'message': 'Товар успешно удален из заказа'})
        else:
            return HttpResponse('Товар с таким id не найден в заказе', status=404)

    except Http404:
        return HttpResponse('Отсутствует заказ или товар с таким id', status=404)
    except Exception as e:
        return HttpResponse(f'ОШИБКА: {str(e)}', status=500)


# ========================================Delete===================================================
def delete_client(request, client_id):
    try:
        client = Client.objects.get(id=client_id)
        client_name = client.name
        client.delete()
        html = "<html><body>Клиент {} с id {} успешно удален</body></html>".format(client_name, client_id)
        return HttpResponse(html)
    except Client.DoesNotExist:
        return HttpResponse("Клиент с id {} отсутствует в базе данных".format(client_id))
    except Exception as e:
        return HttpResponse("ОШИБКАСЪ: {}".format(e))


def delete_product(request, product_id):
    try:
        product = Product.objects.get(id=product_id)
        product.delete()
        html = "<html><body>Товар с id {} успешно удален</body></html>".format(product_id)
        return HttpResponse(html)
    except Product.DoesNotExist:
        return HttpResponse("Товар с id {} отсутствует в базе данных".format(product_id))
    except Exception as e:
        return HttpResponse("ОШИБКАСЪ: {}".format(e))


def delete_order(request, order_id):
    try:
        order = Order.objects.get(id=order_id)
        order.delete()
        html = "<html><body>Заказ с id {} успешно удален</body></html>".format(order_id)
        return HttpResponse(html)
    except Order.DoesNotExist:
        return HttpResponse("Заказ с id {} отсутствует в базе данных".format(order_id))
    except Exception as e:
        return HttpResponse("ОШИБКАСЪ: {}".format(e))


# =====================================
def all_orders(request, client_id):
    client = Client.objects.get(pk=client_id)
    orders = Order.objects.filter(client=client)
    context = {
        "orders": orders,
        "client_name": client.name}
    return render(request, "homework_app/orders_client.html", context)


def show_order(request, order_id):
    order = Order.objects.get(pk=order_id)
    order_products = order.products.all()
    context = {
        "order": order,
        "order_products": order_products}
    return render(request, "homework_app/order_info.html", context)


def order_list(request, client_id):
    # принимаем 2 параметра, проверяем, что клиент является объектом Client c id таким-то, иначе 404
    client = get_object_or_404(Client, pk=client_id)

    # инициализируем заказы, отфильтрованные по периодам
    orders = {
        '7_days': Order.objects.filter(client=client,
                                       order_date__gte=datetime.datetime.now() - datetime.timedelta(days=7)).order_by(
            'order_date'),
        '30_days': Order.objects.filter(client=client,
                                        order_date__gte=datetime.datetime.now() - datetime.timedelta(days=30)).order_by(
            'order_date'),
        '365_days': Order.objects.filter(client=client, order_date__gte=datetime.datetime.now() - datetime.timedelta(
            days=365)).order_by('order_date')
    }
    # инициализируем пустой словарь, где будут лежать уникальные товары для каждого заказа
    orders_with_products = {}
    #  проходимся циклом по элементам в словаре заказов orders
    for key, value in orders.items():
        unique_products = set()  # инициализируем  множество для хранения уникальных товаров
        # тут перебираем каждый заказ и товары в заказе и добавляем их в множество
        for order in value:
            for product in order.products.all():
                unique_products.add((product.name, product.id))  # добавляем кортеж из имени и id товара
        unique_products_list = list(unique_products)  # конвертируем в список
        unique_products_list.sort(key=lambda x: x[1])  # Сортировка товаров по ID по возрастанию
        orders_with_products[key] = unique_products_list  # присваиваем список товаров своему ключу
        # визуализируем заготовленный шаблон, передавая в него заказы с товарами
    return render(request, 'homework_app/order_list.html', {
        'client_name': client.name,
        'orders_with_products': orders_with_products
    })


# Доработаем задачу про клиентов, заказы и товары из
# прошлого семинара.
# Создайте форму для редактирования товаров в базе
# данных.
#  Измените модель продукта, добавьте поле для хранения
# фотографии продукта.
#  Создайте форму, которая позволит сохранять фото.
def edit_product(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            if 'photo' not in request.FILES:
                product.photo = 'homework_app/product_photos/default_image.jpg'
            form.save()
    else:
        form = ProductForm(instance=product)
    return render(request, 'homework_app/edit_product.html', {'form': form, 'name': product.name})

