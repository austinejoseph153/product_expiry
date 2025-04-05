from django.contrib import admin
from .models import Product, Batch

@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', "category", "price")
    ordering = ["-id"]

