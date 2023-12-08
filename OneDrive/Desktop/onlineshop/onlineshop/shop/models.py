from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    name = models.CharField(max_length=200, null=True)
    email = models.EmailField(unique=True, null=True)
    bio = models.TextField(null=True)
    avator = models.ImageField(null=True, upload_to='profile/', default="profile/avatar.svg")

    # USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []


class Categorie(models.Model):
    category_name = models.CharField(max_length=50)
    category_description = models.TextField()
    category_Items = models.IntegerField()
    category_image = models.ImageField(upload_to='category/', default='img/cat-1.jpg')


class Manufacture(models.Model):
    manufacture_name = models.CharField(max_length=50)
    manufacture_Description = models.TextField()


class Product(models.Model):
    product_name = models.CharField(max_length=50)
    product_image = models.ImageField(upload_to='productImage/', default='img/cat-1.jpg')
    Product_description = models.TextField(null=True)
    product_price = models.IntegerField()
    product_previous_price = models.IntegerField(null=True)
    product_additional_information = models.TextField()
    product_size = models.CharField(max_length=30)
    product_manufacture = models.ForeignKey(Manufacture, on_delete=models.CASCADE)
    product_category = models.ForeignKey(Categorie, on_delete=models.CASCADE)
    product_items = models.IntegerField()
    product_owner = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name="owner")
    product_color = models.CharField(max_length=40)


class ProductImages(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(null=True)


class SuperUsers(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="superuser")


class Cart(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    time = models.DateTimeField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="customer")


class Favorite(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    time = models.DateTimeField()


class Messages(models.Model):
    sender = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name="sender")
    message = models.TextField()
    time = models.DateTimeField()


class Sales(models.Model):
    pass


class Suggestions(models.Model):
    pass


class Transactions(models.Model):
    pass


class SpecialOffer(models.Model):
    pass


class Couponcode(models.Model):
    pass


class Reviews(models.Model):
    product_reviews = models.ForeignKey(Product, on_delete=models.CASCADE)
