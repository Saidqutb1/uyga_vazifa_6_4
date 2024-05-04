from django.shortcuts import render, redirect
from .forms import ProductForm
from .models import Category, Products
# Create your views here.


def get_info(request):
    categories = Category.objects.all()
    context = {
        'categories': categories
    }
    return render(request, 'index.html', context=context)

def get_products(request, pk):
    products = Products.objects.filter(category=pk)
    contex = {
        'product': products
    }
    return render(request, 'product.html', context=contex)

def detail(request, pk):
    product = Products.objects.get(pk=pk)
    context = {
        'product': product
    }
    return render(request, 'detail.html', context=context)

def add_products(request):
    form = ProductForm(request.POST, request.FILES)
    if form.is_valid():
        form.save()
        return redirect('products:get_info')
    context = {
        'form': form
    }
    return render(request, 'create.html', context=context)

def update_products(request, pk):
    data = Products.object.get(pk=pk)
    form = ProductForm(request.POST, request.FILES, instance=data)
    if form.is_valid():
        print(1)
        form.save()
        return redirect('products:get_info')
    context = {
        'form': form
    }

    return render(request, 'update.html', context=context)






