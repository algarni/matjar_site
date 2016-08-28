from django.shortcuts import render
from django.http import HttpResponse
from .forms import ProductForm
from django.views.generic import ListView
from matjar.models import Product


# def index(request):
#     return render(request, 'dashboard/product/product_list.html', {})


class ProductList(ListView):
    model = Product
    template_name = 'dashboard/product/product_list.html'
    context_object_name = 'product_list'


def create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return HttpResponse('The product has been saved.')

    form = ProductForm()
    return render(request, 'dashboard/product/create.html', {'form': form})
