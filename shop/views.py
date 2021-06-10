from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.http import JsonResponse
from product.models import Product, User, Customer, Order, OrderItem
from shop.models import Shop

# Create your views here.


def shop(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        customer = request.user.customer
        customerName = customer.name
        order, created = Order.objects.get_or_create(
            customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items

    else:
        customerName = ''
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0}
        cartItems = order['get_cart_items']
    shops = Shop.objects.all()
    context = {'cartItems': cartItems,
               'customerName': customerName, 'shops': shops}
    return render(request, 'shop/shop.html', context)


def shopProduct(request, shopurl):
    if request.user.is_authenticated:
        customer = request.user.customer
        customer = request.user.customer
        customerName = customer.name
        order, created = Order.objects.get_or_create(
            customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items

    else:
        customerName = ''
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0}
        cartItems = order['get_cart_items']
    shop = Shop.objects.get(shopurl=shopurl)
    products = shop.product_set.all()
    context = {'cartItems': cartItems,
               'customerName': customerName, 'shop': shop, 'products': products}
    return render(request, 'shop/shop_product.html', context)
