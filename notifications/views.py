from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Products
from .utils import get_db_handle


def product_list(request):
    # db_handle = get_db_handle('your_database_name', 'your_host', 'your_username', 'your_password')
    db_handle, client = get_db_handle('soltase', 'store1')
    products = db_handle['Products'].find()
    product_names = [product['name'] for product in products]
    
    print("product_names", product_names)
    context = {
        'product_names': product_names,
    }
    return render(request, 'notifications/products.html', context)

def test(request):
    template = loader.get_template('myfirst.html')
    return HttpResponse(template.render())


def notifications(request):
    return HttpResponse("Hello world!")

