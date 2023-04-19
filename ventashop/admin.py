from django.contrib import admin

from .models import Category, Product, LineItem, Cart, Order, Comment

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    fields = ["name"]


admin.site.register(Category, CategoryAdmin)


class ProductAdmin(admin.ModelAdmin):
    fields = ["name", "date_created", "description", "price", "category"]


admin.site.register(Product, ProductAdmin)


class LineItemAdmin(admin.ModelAdmin):
    fields = ["product", "quantity", "price", "cart", "order"]


admin.site.register(LineItem, LineItemAdmin)


class CartAdmin(admin.ModelAdmin):
    fields = ["total_price"]


admin.site.register(Cart, CartAdmin)


class OrderAdmin(admin.ModelAdmin):
    fields = ["status", "total_price", "date_created", "ref_number"]


admin.site.register(Order, OrderAdmin)


class CommentAdmin(admin.ModelAdmin):
    fields = ["content", "date_created", "order"]


admin.site.register(Comment, CommentAdmin)