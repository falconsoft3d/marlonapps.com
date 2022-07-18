from django.db import models
from base.models import BaseClass
# Create your models here.

class Category(BaseClass):
    category_name = models.CharField(max_length=20, unique=True)
    description = models.CharField(max_length=255, blank=True)
    slug = models.CharField(max_length=100, unique=True)
    cat_image = models.ImageField(upload_to='photos/categories', blank = True)
    
    def __str__(self):
        return '{}'.format(self.category_name)
    
    def save(self):
        self.category_name = self.category_name.upper()
        super(Category, self).save()
    
    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'
    
    def __str__(self):
        return self.category_name