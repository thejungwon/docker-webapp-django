from django.contrib import admin
from .models import Post, Pizza
from .domain.models import Address, Courier, DrinkProduct, EmailTemplate, FoodProduct, Ingredient, Order, OrderItem, \
    PriviligeLevel, Transaction, User, UserPizza

# Register your models here.
admin.site.register(Post)
admin.site.register(Pizza)
admin.site.register(Address)
admin.site.register(Courier)
admin.site.register(DrinkProduct)
admin.site.register(EmailTemplate)
admin.site.register(FoodProduct)
admin.site.register(Ingredient)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(PriviligeLevel)
admin.site.register(Transaction)
admin.site.register(User)
admin.site.register(UserPizza)
