from django.urls import path

from . import views

urlpatterns = [
    path('product/', views.product, name='product'),
    path('cart/', views.cart, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('orders/', views.orders, name='orders'),

    path('update_item/', views.updateItem, name="update_item")
]
