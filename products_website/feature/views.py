from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from django.views import generic

from .models import *


class Index_view(generic.ListView):
    template_name = "feature/index.html"
    queryset = Categories.objects.order_by('name')


class Product_Detail(generic.DetailView):
    template_name = "feature/detail_product.html"
    model = Products


class Products(generic.ListView):
    template_name = "feature/products.html"
    queryset = Products.objects.order_by('name')


class Orders(generic.ListView):
    template_name = "feature/orders.html"
    queryset = Others.objects.order_by('date')


class OrderDetail(generic.DetailView):
    template_name = "feature/order_detail.html"
    model = Others


class OrderUpdate(generic.UpdateView):
    model = Others
    fields =['status','total','session']
    template_name_suffix = '_update_form'


class OrderDelete(generic.DeleteView):
    model = Others
    

class OrderCreate(generic.CreateView):
    model= Others
    fields=['date','status','total','session']

class Customer_order(generic.DetailView):
    model = Customers
    template_name = "feature/customer_order.html"