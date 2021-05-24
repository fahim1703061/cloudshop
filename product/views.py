from django.shortcuts import render

# Create your views here.


def product(request):
    context = {}
    return render(request, 'product/product.html', context)


def cart(request):
    context = {}
    return render(request, 'product/cart.html', context)


def checkout(request):
    context = {}
    return render(request, 'product/checkout.html', context)
