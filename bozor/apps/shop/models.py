from django.db import models


class Category ( models.Model ):
    title = models.CharField ( max_length=50 )
    slug = models.SlugField ( unique=True )

    def __str__(self):
        return self.title


class SubCategory ( models.Model ):
    Category = models.ForeignKey ( Category , on_delete=models.SET_NULL , null=True )
    title = models.CharField ( max_length=50 )
    slug = models.SlugField ( unique=True )

    def __str__(self):
        return self.title


class Product ( models.Model ):
    Category = models.ForeignKey ( Category , on_delete=models.SET_NULL , null=True )
    SubCategory = models.ForeignKey ( SubCategory , on_delete=models.SET_NULL , null=True )
    title = models.CharField ( max_length=200 )
    tags = models.CharField ( max_length=200, default='')
    description = models.TextField ()
    price = models.DecimalField ( decimal_places=2 , max_digits=10 )
    stock = models.PositiveIntegerField ()
    image = models.ImageField ( upload_to='product' , null=True , blank=True )

    def __str__(self):
        return self.title
