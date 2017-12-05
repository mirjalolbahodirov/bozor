from django.contrib import admin
from .models import Category, Product


# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ['title']}
    list_display = ['id', 'title', 'slug']


class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'price', 'stock']


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
