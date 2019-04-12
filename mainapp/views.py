# Create your views here.

from django.shortcuts import render, get_object_or_404
from mainapp.models import ProductCategory, Product
from basketapp.models import Basket


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
    basket = Basket.objects.filter(user=request.user)

    my_context = {
        'title': links_menu[0]['title'],
        'links_menu': links_menu,
        'products': products,
        'trending_products': trending_products,
        'basket': basket
    }
    return render(request, 'index.html', my_context)


def products_view(request, pk=None):

    links_categories = ProductCategory.objects.all()
    basket = Basket.objects.filter(user=request.user)

    if pk is not None:
        if pk == 0:
            products = Product.objects.all().order_by('price')
            category = {'name': 'all'}
        else:
            category = get_object_or_404(ProductCategory, pk=pk)
            products = Product.objects.filter(category__pk=pk).order_by('price')

        my_context = {
            'title': links_menu[1]['title'],
            'links_menu': links_menu,
            'links_categories': links_categories,
            'category': category,
            'products': products,
            'basket': basket
        }

        return render(request, 'mainapp/products_list.html', my_context)

    else:
        same_products = Product.objects.all()[:12]

        my_context = {
            'title': links_menu[1]['title'],
            'links_menu': links_menu,
            'links_categories': links_categories,
            'same_products': same_products,
            'basket': basket
        }

        return render(request, 'mainapp/products.html', my_context)


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

    basket = Basket.objects.filter(user=request.user)

    my_context = {
        'title': links_menu[4]['title'],
        'links_menu': links_menu,
        'basket': basket
    }

    return render(request, 'contact.html', my_context)