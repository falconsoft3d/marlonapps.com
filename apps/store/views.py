from unicodedata import category
from django.shortcuts import get_object_or_404, render
from apps.store.models import Product
from category.models import Category

# Create your views here.
def store(request, category_slug=None):
    categories = None
    products = None
    
    if category_slug != None:
        categories = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=categories, state=True)
        product_count = products.count()
    else:
        products = Product.objects.all().filter(state=True)
        product_count = products.count()
    
    context = {
        'products' : products,
        'product_count' : product_count
    }
    
    return render(request, 'store/store.html', context)

def product_detail(request, category_slug=None, product_slug=None):
    return render(request, 'store/product_detail.html')
