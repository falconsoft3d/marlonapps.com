from ast import keyword
from importlib.resources import contents
from itertools import product
from unicodedata import category
from django.shortcuts import get_object_or_404, render
from apps.store.models import Product
from category.models import Category
from carts.views import _cart_id
from carts.models import CartItem
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db.models import Q

# Create your views here.
def store(request, category_slug=None):
    categories = None
    products = None
    
    if category_slug != None:
        categories = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=categories, state=True).order_by('-fc')
        paginator = Paginator(products, 6)
        page = request.GET.get('page')
        paged_products = paginator.get_page(page)
        product_count = products.count()
    else:
        products = Product.objects.all().filter(state=True).order_by('-fc')
        paginator = Paginator(products, 6)
        page = request.GET.get('page')
        paged_products = paginator.get_page(page)
        product_count = products.count()
    
    context = {
        'products' : paged_products,
        'product_count' : product_count
    }
    
    return render(request, 'store/store.html', context)

def product_detail(request, category_slug, product_slug):
    try:
        single_product = Product.objects.get(category__slug=category_slug, slug=product_slug)
        in_cart = CartItem.objects.filter(cart__cart_id=_cart_id(request), product=single_product).exists
    
    except Exception as e:
        raise e
    
    context = {
        'single_product' : single_product,
        'in_cart' : in_cart
    }
    
    return render(request, 'store/product_detail.html', context)

def search(request):
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            products = Product.objects.order_by('-fc').filter(Q(description__icontains=keyword) | Q(product_name__icontains=keyword))
            product_count = products.count()
        else:
            products = Product.objects.order_by('-fc')
            product_count = products.count()
             
    context = {
        'products' : products,
        'product_count' : product_count
    }
    
    return render(request, 'store/store.html', context)
