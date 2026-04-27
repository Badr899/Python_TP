from django.shortcuts import render
from .models import Product
from django.views import View
from django.views.generic import ListView,DetailView

class ProductListView(ListView):
    model = Product
    template_name = 'products/product_list.html'
    context_object_name = 'products'


class ProductDetailView(DetailView):
    model = Product
    template_name = 'products/product_detail.html'
    context_object_name = 'product'
    
