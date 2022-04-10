from django.db import models

class Category(models.Model):
    name       = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'categories'

class Product(models.Model):
    category    = models.ForeignKey('Category', on_delete=models.CASCADE)
    name        = models.CharField(max_length=300)
    origin      = models.CharField(max_length=300)
    volume      = models.CharField(max_length=300)
    description = models.TextField()
    summary     = models.TextField()
    price       = models.DecimalField(max_digits=10, decimal_places=2)
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'products'


class Image(models.Model):
    product    = models.ForeignKey('Product', on_delete=models.CASCADE)
    image_url  = models.CharField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta: 
        db_table = 'images'  