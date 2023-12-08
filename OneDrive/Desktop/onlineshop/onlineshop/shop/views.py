import random
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q
from django.shortcuts import render

from shop.models import Product


# Create your views here.


import random

def home(request):
    products = list(productsserch(request, "all"))
    if request.method == "POST":
        query = request.POST.get('search')
        products = list(productsserch(request, query))
    highlights = random.sample(products, min(4, len(products)))
    while len(highlights) < 5:
        additional_products = list(productsserch(request, "all"))
        print("Additional Products:", additional_products)
        highlights.extend(random.sample(additional_products, min(5 - len(highlights), len(additional_products))))
    context = {"products": products, "highlights": highlights}
    return render(request, 'shop/index.html', context)



def details(request):
    return render(request, 'shop/detail.html')


def cart(request):
    return render(request, 'shop/cart.html')


def shop(request):
    return render(request, 'shop/shop.html')


def contact(request):
    return render(request, 'shop/contact.html')


def addproduct(request):
    return render(request, 'shop/addProduct.html')


def about(request):
    return render(request, 'shop/aboutus.html')


def favorites(request):
    return render(request, 'shop/favourites.html')


def productsserch(request, query):
    if query == 'all':
        products = Product.objects.all()
    else:
        try:
            products = Product.objects.filter(
                Q(product_name__icontains=query) | Q(Product_description__icontains=query) | Q(
                    product_manufacture__manufacture_name__icontains=query) | Q(
                    product_owner__username__contains=query) | Q(product_category__category_name__icontains=query) | Q(
                    product_category__category_description__icontains=query))
        except ObjectDoesNotExist:
            products = Product.objects.all()

    return products
