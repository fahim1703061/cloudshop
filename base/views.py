from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.http import JsonResponse
from product.models import Product, User, Customer, Order, OrderItem
import json
import datetime
# Create your views here.


@csrf_exempt
def test(request):

    return HttpResponse("payment Completed.Go to <a href=\"http://127.0.0.1:8000\">cloudshop</a>")


def index(request):

    if request.user.is_authenticated:
        customer = request.user.customer
        customerName = customer.name
        # print(customerName)

        pastOrders = Order.objects.filter(
            customer=customer, complete=True)

        # customer = request.user.customer
        pastOrders = list(reversed(pastOrders))
        print(pastOrders[0].get_cart_total)
        print(datetime.datetime.now())
        totalAmount = pastOrders[0].get_cart_total

    else:
        customerName = ''
        totalAmount = 0

    from sslcommerz_lib import SSLCOMMERZ
    settings = {'store_id': 'testbox',
                'store_pass': 'qwerty', 'issandbox': True}
    sslcommez = SSLCOMMERZ(settings)
    post_body = {}
    post_body['total_amount'] = totalAmount
    post_body['currency'] = "BDT"
    post_body['tran_id'] = "12345"
    post_body['success_url'] = "http://127.0.0.1:8000/baselite/"
    post_body['fail_url'] = "your fail url"
    post_body['cancel_url'] = "your cancel url"
    post_body['emi_option'] = 0
    post_body['cus_name'] = "test"
    post_body['cus_email'] = "test@test.com"
    post_body['cus_phone'] = "01714461921"
    post_body['cus_add1'] = "customer address"
    post_body['cus_city'] = "Dhaka"
    post_body['cus_country'] = "Bangladesh"
    post_body['shipping_method'] = "NO"
    post_body['multi_card_name'] = ""
    post_body['num_of_item'] = 1
    post_body['product_name'] = "Test"
    post_body['product_category'] = "Test Category"
    post_body['product_profile'] = "general"

    response = sslcommez.createSession(post_body)
    print(response['GatewayPageURL'])

    if(response['GatewayPageURL']):
        return redirect(response['GatewayPageURL'])

    # context = {'post_body': post_body}
    context = {}
    return render(request, 'index.html', context)


# def sslreq(request):
#     if(request.POST):

#         if(response['GatewayPageURL']):
#             return JsonResponse({'status': 'success', 'data': response['GatewayPageURL'], 'logo': response['storeLogo']})
#         else:
#             print('failed')

#         return JsonResponse({'status': 'success', 'data': response['GatewayPageURL'], 'logo': response['storeLogo']})


def home(request):
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
    products = Product.objects.all()
    context = {'products': products, 'cartItems': cartItems,
               'customerName': customerName}
    return render(request, 'base/home.html', context)
