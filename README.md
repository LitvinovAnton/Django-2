Домашняя работа 2. Модели <br>
Созданы модели 'Клиент', 'Товар', 'заказ' с требуемыми для них полями <br>
Реализованы CRUD функции для этих моделей: <br>
<pre>Create - расположены в файле homework_app/management/commands/my_command.py <br>
при выполнении команды  "python3 manage.py my_command" создаётся 10 клиентов с рандомными данными, <br>
создаётся 10 позиций товаров с рандомными данными, и для каждого клиента создается 1 заказ,  <br>
с рандомным количеством товаров. Товары в заказе располагаются в связующей таблице order.products <br></pre>
<pre>Read - в файле homework_app/views.py методы: get_client(), get_product(), get_order(), products_by_order(), <br>
get_all_clients(), get_all_products(), get_all_orders(). Позволяют через url получить данные клиента,  <br>
данные товара, данные заказа, еще можно получить таблицу всех клиентов или всех товаров или всех заказов.  <br>
также получить таблицу товаров в определенном заказе <br></pre>
**Примеры Read запросов:** <br>
http://89.23.115.214:8000/get_clients/  - таблица клиентов <br>
http://89.23.115.214:8000/get_client/17/  - карточка клиента <br>
http://89.23.115.214:8000/get_products/  - таблица товаров <br>
http://89.23.115.214:8000/get_product/21/  - карточка товара <br>
http://89.23.115.214:8000/get_orders/  - таблица заказов <br>
http://89.23.115.214:8000/get_order/37/  - карточка заказа <br>
http://89.23.115.214:8000/products_by_order/37/  - отдельно товары заказа <br>
    <pre> Update - в файле homework_app/views.py методы: update_name_client(), update_price_product(),  <br>
add_product_to_order(), remove_product_from_order(). Методы позволяют изменить через url: имя клиента, 
изменить цену определенного товара, также можно добавить товар в имеющийся заказ или удалить товар из заказа. <br></pre>
**Примеры Update запросов:** <br>
http://89.23.115.214:8000/update_order/37/add_product/24/  - добавление товара <br>
http://89.23.115.214:8000/update_order/37/delete_product/24/  - удаление товара <br>
http://89.23.115.214:8000/update_product/21/update_price/11111/  - обновление цены <br>
http://89.23.115.214:8000/update_client/29/update_name/Lotos/  - обновление фио <br>
    <pre>Delete - в файле homework_app/views.py методы: delete_client(), delete_product(), delete_order(). <br>
Тут все просто, удаляется либо клиент, либо товар, либо заказ <br></pre>
    **Примеры delete запросов:** <br>
http://89.23.115.214:8000/delete_client/26/  - удаление клиента <br>
http://89.23.115.214:8000/delete_product/53/  - удаление товара <br>
http://89.23.115.214:8000/delete_order/49/  - удаление заказа <br>