from datetime import datetime
from decimal import Decimal

from django.contrib import admin

from django.contrib import admin
from .models import Client, Order, Product


# login - admin, password - 1, email - wogl@mail.ru


class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone_number', 'registration_date')
    search_fields = ('name', 'email', 'phone_number')
    list_filter = ('registration_date', 'address')
    readonly_fields = ('registration_date',)
    fieldsets = (
        (None, {
            'description': 'Имя и почта',
            'fields': ('name', 'email')
        }),
        (
            'Контактная информация',
            {
                'description': 'Номер телефона и адрес',
                'fields': ('phone_number', 'address')
            }),
        (
            'Другая информация',
            {
                'description': 'дата регистрации',
                'fields': ('registration_date',)
            }),
    )


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'quantity', 'added_date')
    search_fields = ('name', 'description')
    list_filter = ('added_date', 'name')
    readonly_fields = ('added_date',)
    fieldsets = (
        (None, {
            'description': 'Название и стоимость',
            'fields': ('name', 'price')
        }),
        (
            'Опись',
            {
                'description': 'Количество и дата добавления',
                'fields': ('quantity', 'added_date')
            }),
        (
            'Описание', {
                'fields': ('description',)
            }),
    )

    @admin.action(description='количество = 1')
    def quantity_1(self, request, queryset):
        queryset.update(quantity=1)

    @admin.action(description='изменение даты')
    def reset_product_date(modeladmin, request, queryset):
        queryset.update(added_date=datetime.now())

    actions = [quantity_1, reset_product_date]


class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'client', 'total_amount', 'order_date')
    filter_horizontal = ('products',)
    list_filter = ('order_date', 'client')

    fieldsets = (
        (
            None, {
                'description': 'покупатель и дата заказа',
                'fields': ('client', 'order_date')
            }),
        (
            'Товары', {
                'description': 'список товаров',
                'fields': ('products',)
            }),
        (
            'Стоимость', {
                'description': 'Итоговая сумма',
                'fields': ('total_amount',)
            }),
    )


admin.site.register(Client, ClientAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)
