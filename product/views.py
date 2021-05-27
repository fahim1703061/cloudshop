from django.shortcuts import render
from .models import Product

# Create your views here.


def product(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'product/product.html', context)


def cart(request):
    context = {}
    return render(request, 'product/cart.html', context)


def checkout(request):
    context = {}
    return render(request, 'product/checkout.html', context)
