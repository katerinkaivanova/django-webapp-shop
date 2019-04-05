# Create your views here.

from django.shortcuts import render
from .models import ProductCategory, Product

links_menu = [
    {'href': 'main', 'title': 'home'},
    {'href': 'products:index', 'namespace': 'products', 'title': 'products'},
    {'href': 'history', 'title': 'history'},
    {'href': 'showroom', 'title': 'showroom'},
    {'href': 'contact', 'title': 'contact'}
]

def main_view(request):
    products = Product.objects.all()[:4]
    trending_products = Product.objects.all()[:6]

    my_context = {
        'title': links_menu[0]['title'],
        'links_menu': links_menu,
        'products': products,
        'trending_products': trending_products
    }
    return render(request, 'index.html', my_context)


def products_view(request):
    products = Product.objects.all()[:12]
    links_categories = ProductCategory.objects.all()

    my_context = {
        'title': links_menu[1]['title'],
        'links_menu': links_menu,
        'links_categories': links_categories,
        'products': products
    }
    return render(request, 'products.html', my_context)

def history_view(request):
    my_context = {
        'title': links_menu[2]['title'],
        'links_menu': links_menu
    }
    return render(request, 'history.html', my_context)


def showroom_view(request):
    my_context = {
        'title': links_menu[3]['title'],
        'links_menu': links_menu
    }
    return render(request, 'showroom.html', my_context)

def contact_view(request):
    my_context = {
        'title': links_menu[4]['title'],
        'links_menu': links_menu
    }
    return render(request, 'contact.html', my_context)