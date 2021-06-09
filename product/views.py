from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Product, User, Customer, Order, OrderItem
import json
import datetime
from .forms import ShippingAddressForm

# Create your views here.


def product(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        customerName = customer.name
        order, created = Order.objects.get_or_create(
            customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items

    else:
        customerName = ''
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0, 'shipping': False}
        cartItems = order['get_cart_items']
    products = Product.objects.all()
    context = {'products': products, 'cartItems': cartItems,
               'customerName': customerName}
    return render(request, 'product/product.html', context)


def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        customerName = customer.name
        order, created = Order.objects.get_or_create(
            customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items

    else:
        customerName = ''
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0, 'shipping': False}
        cartItems = order['get_cart_items']
        # print('not authenticaed')

    context = {'items': items, 'order': order,
               'cartItems': cartItems, 'customerName': customerName}
    return render(request, 'product/cart.html', context)


def checkout(request):
    print(request.POST)
    if request.user.is_authenticated:
        customer = request.user.customer
        customerName = customer.name
        order, created = Order.objects.get_or_create(
            customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
        transaction_id = datetime.datetime.now().timestamp()
        order.transaction_id = transaction_id
        order.complete = True

        form = ShippingAddressForm()
        if request.method == 'POST':

            print('post')
            form = ShippingAddressForm(request.POST)
            if form.is_valid():  # All validation rules pass
                # Process the data in form.cleaned_data
                # ...

                new_object = form.save(commit=False)
                order.data_ordered = datetime.datetime.now()
                order.save()
                new_object.customer = customer
                new_object.order = order
                new_object.save()

                print(form.cleaned_data["address"])
                print(new_object.phone)

                return redirect('/')
            else:
                print('not valid............')

    else:
        customerName = ''
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0, 'shipping': False}
        cartItems = order['get_cart_items']
        # print('not authenticaed')

    context = {'items': items, 'order': order,
               'cartItems': cartItems, 'customerName': customerName}
    return render(request, 'product/checkout.html', context)


def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']
    print('Action:', action)
    print('Product:', productId)

    customer = request.user.customer
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(
        customer=customer, complete=False)

    orderItem, created = OrderItem.objects.get_or_create(
        order=order, product=product)

    if action == 'add':
        orderItem.quantity = (orderItem.quantity + 1)
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity - 1)

    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete()

    return JsonResponse('Item was added', safe=False)


def orders(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        customerName = customer.name
        # print(customerName)
        orderget, created = Order.objects.get_or_create(
            customer=customer, complete=False)
        items = orderget.orderitem_set.all()
        cartItems = orderget.get_cart_items

        pastOrders = Order.objects.filter(
            customer=customer, complete=True)

        # customer = request.user.customer
        pastOrders = list(reversed(pastOrders))
        print(pastOrders[0].id)
        print(datetime.datetime.now())

    else:
        customerName = ''
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0, 'shipping': False}
        cartItems = order['get_cart_items']
        pastOrders = []
    products = Product.objects.all()
    context = {'products': products,
               'cartItems': cartItems, 'pastOrders': pastOrders, 'customerName': customerName}

    return render(request, 'product/orders.html', context)
