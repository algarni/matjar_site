from django.shortcuts import render
from django.http import HttpResponseRedirect
# from dashboard.category.forms import CategoryForm
from django.views.generic import ListView
from django.views.generic.edit import CreateView, FormView
from matjar.models import Category


# def index(request):
#     return render(request, 'dashboard/category/category_list.html')


class CategoryList(ListView):
    model = Category
    context_object_name = 'category_list'
    template_name = 'dashboard/category/category_list.html'


# def create(request):
#     if request.method == 'POST':
#         form = CategoryForm(request.POST)
#
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect('/dashboard/category/')
#
#     else:
#         form = CategoryForm()
#
#     return render(request, 'dashboard/category/category_create.html', {'form': form})


class CategoryCreate(CreateView):
    model = Category
    fields = ['name']
    template_name = 'dashboard/category/category_create.html'
    success_url = '/dashboard/category/'

