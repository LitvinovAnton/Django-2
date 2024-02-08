import datetime
import logging
import random

from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse, JsonResponse, Http404
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
import pytz

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
    # Create an HTML table to display the product details
    html = f"""
    <h2>Карточка товара</h2>
    <table>
        <tr>
            <th>ID Товара</th>
            <th>Название</th>
            <th>Описание</th>
            <th>цена</th>
        </tr>
        <tr>
            <td>{product.id}</td>
            <td>{product.name}</td>
            <td>{product.description}</td>
            <td>{product.price}</td>
        </tr>
    </table>
    """
    return HttpResponse(html)


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
