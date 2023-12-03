from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('details/', views.details, name='details'),
    path('cart/', views.cart, name='cart'),
    path('shop/', views.shop, name='shop'),
    path('contact/', views.contact, name='contact'),
]
