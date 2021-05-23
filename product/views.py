from django.shortcuts import render

# Create your views here.


def product(request):
    context = {}
    return render(request, 'product/product.html', context)
