from django.contrib import admin
from . import models

# Register your models here.

admin.site.register(models.User)
admin.site.register(models.Cart)
admin.site.register(models.Sales)
admin.site.register(models.Product)
admin.site.register(models.Categorie)
admin.site.register(models.Favorite)
admin.site.register(models.Messages)
admin.site.register(models.ProductImages)
admin.site.register(models.Suggestions)
admin.site.register(models.SuperUsers)
admin.site.register(models.Transactions)
