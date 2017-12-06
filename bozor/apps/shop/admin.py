from django.contrib import admin

from .models import Category , Product , SubCategory


# Register your models here.

class CategoryAdmin ( admin.ModelAdmin ):
    prepopulated_fields = {'slug': ['title']}
    list_display = ['id' , 'title' , 'slug']


class SubCategoryAdmin ( admin.ModelAdmin ):
    prepopulated_fields = {'slug': ['title']}
    list_display = ['id' , 'Category' , 'title' , 'slug' , ]


class ProductAdmin ( admin.ModelAdmin ):
    list_display = ['id' , 'Category' , 'SubCategory' , 'title' , 'price' , 'stock']


admin.site.register ( Category , CategoryAdmin )
admin.site.register ( Product , ProductAdmin, )
admin.site.register ( SubCategory , SubCategoryAdmin )
