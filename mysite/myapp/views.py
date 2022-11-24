from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Product


def index(request):
    return HttpResponse("Hello World")


def products(request):
    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(request, 'myapp/index.html', context)


def product_detail(request, id):
    product = Product.objects.get(id=id)
    context = {
        'product': product
    }
    return render(request, 'myapp/detail.html', context)


def add_product(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        price = request.POST.get('price')
        desc = request.POST.get('desc')
        image = request.FILES['upload']
        product = Product(name=name, price=price, desc=desc, image=image)
        product.save()

    return render(request, 'myapp/addproduct.html')

def update_product(request, id):
    
    product = Product.objects.get(id=id)
    if request.method == 'POST':
        product.name = request.POST.get('name')
        product.price = request.POST.get('price')
        product.desc = request.POST.get('desc')
        if request.FILES.get('upload') : product.image = request.FILES['upload']
        product.save()
        return redirect('/myapp/products')
    
    context = {
        'product': product,
    }
    return render(request, 'myapp/updateproduct.html', context)
