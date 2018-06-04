from django.shortcuts import render
from .models import Product
from django.shortcuts import redirect
# Create your views here.

def type_list(request):
    products = Product.objects.filter(type__isnull = False)
    return render(request, 'viewdata/type_list.html', {'products':products})

def drink_list(request):
    drinks = Product.objects.filter(type = 'Trinken')
    return render(request, 'viewdata/drink_list.html', {'drinks':drinks})

def chocolate_list(request):
    chocolates = Product.objects.filter(type = 'Schokolade')
    return render(request, 'viewdata/chocolate_list.html', {'chocolates':chocolates})

def chips_list(request):
    chips = Product.objects.filter(type = 'Chips')
    return render(request, 'viewdata/chips_list.html', {'chips':chips})

def biscuit_list(request):
    biscuits = Product.objects.filter(type = 'Kekse')
    return render(request, 'viewdata/biscuit_list.html', {'biscuits':biscuits})

def other_list(request):
    other = Product.objects.filter(type = 'Anderes')
    return render(request, 'viewdata/other_list.html', {'other':other})
"""
url(r'^$', views.type_list, name='typelist_list'),
url(r'^/drinks/$', views.drink_list, name='drink_list'),
url(r'^/chocolate/$', views.chocolate_list, name='chocolate_list'),
url(r'^/chips/$', views.chips_list, name='chips_list'),
url(r'^/biscuits/$', views.biscuits_list, name='biscuits_list'),
url(r'^/other_food/$', views.other_food_list, name='other_food_list'),


url(r'^/chocolate/$', views.chocolate_list, name='chocolate_list'),
    url(r'^/chips/$', views.chips_list, name='chips_list'),
    url(r'^/biscuits/$', views.biscuits_list, name='biscuits_list'),
    url(r'^/other_food/$', views.other_food_list, name='other_food_list'),
"""
