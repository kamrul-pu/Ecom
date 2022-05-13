from django.shortcuts import render
from . import models
# Create your views here.

def store(request):
    products = models.Product.objects.all()
    context = {'products':products}
    return render(request,'store/store.html',context=context)


def cart(request):
    context = {}
    return render(request,'store/cart.html',context=context)

def checkout(request):
    context = {}
    return render(request,'store/checkout.html',context=context)