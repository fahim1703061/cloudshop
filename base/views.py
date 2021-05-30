from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from product.models import Product, User, Customer, Order, OrderItem
import json
# Create your views here.


def test(request):
    return HttpResponse("hello world!")


def index(request):
    return render(request, 'index.html')


def home(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(
            customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items

    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0}
        cartItems = order['get_cart_items']
    products = Product.objects.all()
    context = {'products': products, 'cartItems': cartItems}
    return render(request, 'base/home.html', context)
