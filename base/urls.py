from django.urls import path

from . import views

urlpatterns = [
    path('baselite/', views.test, name='test'),
    # path('', views.index, name='index'),
    path('', views.home, name='home'),

]
