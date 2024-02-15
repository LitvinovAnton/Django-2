from django.urls import path, include

from . import views

from django.conf.urls.static import static
from django.conf import settings
# from ..homework_project import settings

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('get_clients/', views.get_all_clients, name='Клиенты'),
    path('get_client/<int:client_id>/', views.get_client, name='клиент по id'),
    path('get_products/', views.get_all_products, name='Товары'),
    path('get_product/<int:product_id>/', views.get_product, name='Товар по id'),
    path('get_order/<int:order_id>/', views.get_order, name='заказ по id'),
    path('get_orders/', views.get_all_orders, name='Заказы'),
    path('products_by_order/<int:order_id>/', views.products_by_order, name='Товары из заказа'),
    path('delete_client/<int:client_id>/', views.delete_client, name='удаление клиента'),
    path('delete_product/<int:product_id>/', views.delete_product, name='удаление товара'),
    path('delete_order/<int:order_id>/', views.delete_order, name='удаление заказа'),
    path('update_order/<int:order_id>/delete_product/<int:product_id>/',
         views.remove_product_from_order, name='удаление товара из заказа'),
    path('update_product/<int:product_id>/update_price/<int:updated_price>/',
         views.update_price_product, name='изменение цены товара'),
    path('update_order/<int:order_id>/add_product/<int:product_id>/',
         views.add_product_to_order, name='добавление товара к заказу'),
    path('update_client/<int:client_id>/update_name/<str:update_name>/',
         views.update_name_client, name='изменение имени клиента'),
    path('orders/<int:client_id>/', views.all_orders, name='all_orders'),
    path('show_order/<int:order_id>/', views.show_order, name='order'),
    path('order_list/<int:client_id>/', views.order_list, name='order_list'),
    path('edit_product/<int:product_id>/', views.edit_product, name='edit_product'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
