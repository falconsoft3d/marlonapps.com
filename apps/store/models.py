from django.db import models
from base.models import BaseClass
from category.models import Category
from accounts.models import Account
from django.urls import reverse

# Create your models here.
class Product(BaseClass):
    product_name = models.CharField(max_length=200, unique=True)
    slug = models.CharField(max_length=200, unique=True)
    description = models.TextField(max_length=500, blank=True)
    price = models.FloatField(default=1)
    images = models.ImageField(upload_to='photos/products', blank=True)
    stock = models.IntegerField(default=0)
    # is_available = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    code = models.CharField(max_length=13, default="-")
    
    def __str__(self):
        return self.product_name
    
    def get_url(self):
        return reverse('product_detail', args=[self.category.slug, self.slug])

