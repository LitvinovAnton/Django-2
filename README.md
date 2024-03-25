### Домашняя страница, вид:
![Пример](images/last_homework/homepage.png) <br>
### облачный сервер Timeweb:
![Пример](images/last_homework/timeweb_cloud.png) <br>
**Nginx служит в качестве обратного прокси-сервера для Gunicorn, обрабатывая статические файлы и перенаправляя запросы к Gunicorn для обработки Python-кода.**
### gunicorn, gunicorn.socket:
![Пример](images/last_homework/gunicorn_and_gunicornsocket.png) <br>
### nginx:
![Пример](images/last_homework/nginx.png) <br> <br> <br>
Домашняя работа 5. Работа с административной панелью <br>
### URL для входа в административную панель:
http://89.23.115.214:8000/admin/
данные для входа сотрудника:
login - employee_1
password - xtnx$FTZ75qxbtZ
### изменения в models.py: добавлено verbose_name, заменены названия переменных на комфортные именования
### изменения в admin.py - реализованы настройки отображения, фильтры, поля "только для чтения". Actions придумал только 2, для Product
### добавлены группы админы, клиенты, сотрудники
![Пример](images/admin_django/admin_groups.png) <br>
### создано несколько пользователей
![Пример](images/admin_django/admin_users.png) <br> <br>

### настроен удобный вид таблиц
![Пример](images/admin_django/admin_clients.png) <br>
![Пример](images/admin_django/admin_orders.png) <br>
![Пример](images/admin_django/admin_products.png) <br> <br>

### Настроены удобные карточки просмотра/редактирования каждой сущности
![Пример](images/admin_django/admin_client.png) <br>
![Пример](images/admin_django/admin_order.png) <br>
![Пример](images/admin_django/admin_product.png) <br>



Домашняя работа 4. Работа с формами <br>
Создайте форму для редактирования товаров в базе
данных. <br>
Появилась форма **ProductForm** <br>
шаблон - edit_product.html, представление - edit_product(), после нажатия на URL:
http://89.23.115.214:8000/edit_product/8/
![Пример](images/edit_product.png) <br>
### После редактирования, без добавления фото, по дефолту изображение заполняется default_image.jpg
![Пример](images/products_without_image.png) <br>
Измените модель продукта, добавьте поле для хранения
фотографии продукта. <br>
Создайте форму, которая позволит сохранять фото. <br>
http://89.23.115.214:8000/edit_product/8/
![Пример](images/edit_product.png) <br>
### После редактирования товаров с добавлением фотографии товара
http://89.23.115.214:8000/get_products/
![Пример](images/all_products.png) <br> 
### Карточка товара, после добавления фото товара
http://89.23.115.214:8000/get_product/7/
![Пример](images/product.png)<br> <br>



Домашняя работа 3. Представления и шаблоны <br>
Задание 7 <br>
Сделать шаблон для вывода всех заказов клиента и списком товаров, внутри каждого заказа: <br>
шаблон - orders_client.html, представление - all_orders(), после нажатия на URL: <br>
http://89.23.115.214:8000/orders/7/ <br>
![Пример](images/orders_client.png) <br>
После перехода по ссылке заказа: шаблон - order_info.html, представление show_order(), 
после нажатия на URL или после выбора заказа из предыдущей страницы: <br>
http://89.23.115.214:8000/show_order/100/ <br>
![Пример](images/order_100.png) <br>
Продолжаем работать с товарами и заказами. <br>
Создайте шаблон, который выводит список заказанных <br>
клиентом товаров из всех его заказов с сортировкой по
времени: <br>
○ за последние 7 дней (неделю) <br>
○ за последние 30 дней (месяц) <br>
○ за последние 365 дней (год) <br>
*Товары в списке не должны повторятся. <br>
шаблон - order_list.html, представление -  order_list(), пример маршрута: <br>
http://89.23.115.214:8000/order_list/7/ <br>
Вид после нажатия на URL выше:
![Пример](images/view.png) <br>
Для того, чтобы было понятно, что товары не повторяются, добавлен вывод id товара <br><br>
не все клиенты в моей базе делали заказы в течении первых 7 дней, создается все рандомно

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
