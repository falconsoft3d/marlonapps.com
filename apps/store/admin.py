from django.contrib import admin
from .models import Product
import admin_thumbnails
# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'price', 'stock',
                    'category','fc' ,'fm', 'state')
    prepopulated_fields = {'slug': ('product_name', )}
    
    
    
admin.site.register(Product, ProductAdmin)
