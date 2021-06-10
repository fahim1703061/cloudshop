from django.urls import path

from . import views

urlpatterns = [
    path('shop/', views.shop, name='shop'),
    path('<slug:shopurl>', views.shopProduct, name='shop_product')
]
