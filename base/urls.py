from django.urls import path

from . import views

urlpatterns = [
    path('baselite/', views.test, name='test'),
    path('index/', views.index, name='index'),
    path('', views.home, name='home'),

    # path('ssl_req/', views.sslreq, name='sslreq')
]
