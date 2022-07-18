from django.shortcuts import render
from apps.store.models import Product

def home(request):
    products = Product.objects.all().filter(state=True).order_by('fc')[:8]
    

    context = {
        'products' : products,
    }
    
    return render(request, 'home.html', context)
    
    