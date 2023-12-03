from django.shortcuts import render


# Create your views here.

def home(request):
    return render(request, 'shop/index.html')


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
