from django.shortcuts import render
from . models import Products
from django.core.paginator import Paginator

# Create your views here.
def index(request):
    return render(request,'index.html')

def list_products(request):
    product_list = Products.objects.all()
    product_pagenator = Paginator(product_list,2)
    product_list = product_pagenator.get_page(2)
    context={
        'product':product_list
    }
    return render(request,'products.html',context)
def detail_product(request):
    return render(request,'product_detail.html')

