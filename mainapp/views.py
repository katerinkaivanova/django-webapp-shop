# Create your views here.

from django.shortcuts import render
from .models import ProductCategory, Product

links_menu = [
    {'href': 'index', 'name': 'home'},
    {'href': 'products', 'name': 'products'},
    {'href': 'history', 'name': 'history'},
    {'href': 'showroom', 'name': 'showroom'},
    {'href': 'contact', 'name': 'contact'}
]

#links_categories = [
#    {'href': 'products_all', 'name': 'all'},
#    {'href': 'products_home', 'name': 'home'},
#    {'href': 'products_office', 'name': 'office'},
#    {'href': 'products_modern', 'name': 'furniture'},
#    {'href': 'products_classic', 'name': 'modern'},
#    {'href': 'products_classic', 'name': 'classic'},
#]

def main_view(request):
    products = Product.objects.all()[:4]
    trending_products = Product.objects.all()[:6]

    my_context = {
        'title': links_menu[0]['name'],
        'links_menu': links_menu,
        'products': products,
        'trending_products': trending_products
    }
    return render(request, 'index.html', my_context)


def products_view(request):
    products = Product.objects.all()[:12]
    links_categories = ProductCategory.objects.all()

    my_context = {
        'title': links_menu[1]['name'],
        'links_menu': links_menu,
        'links_categories': links_categories,
        'products': products
    }
    return render(request, 'products.html', my_context)

def history_view(request):
    my_context = {
        'title': links_menu[2]['name'],
        'links_menu': links_menu
    }
    return render(request, 'index.html', my_context)


def showroom_view(request):
    my_context = {
        'title': links_menu[3]['name'],
        'links_menu': links_menu
    }
    return render(request, 'index.html', my_context)

def contact_view(request):
    my_context = {
        'title': links_menu[4]['name'],
        'links_menu': links_menu
    }
    return render(request, 'contact.html', my_context)