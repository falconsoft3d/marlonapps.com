from django.db import models
from base.models import BaseClass
from django.urls import reverse

# Create your models here.

class Category(BaseClass):
    category_name = models.CharField(max_length=20, unique=True)
    description = models.CharField(max_length=255, blank=True)
    slug = models.CharField(max_length=100, unique=True)
    cat_image = models.ImageField(upload_to='photos/categories', blank = True)
    
    def __str__(self):
        return '{}'.format(self.category_name)
    
    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'
        
    def get_url(self):
        return reverse('products_by_category', args=[self.slug])
    
    def __str__(self):
        return self.category_name