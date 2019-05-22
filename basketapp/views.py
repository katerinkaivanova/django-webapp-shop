from django.shortcuts import render, HttpResponseRedirect, HttpResponse, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.template.loader import render_to_string
from django.http import JsonResponse
from django.urls import reverse

from basketapp.models import Basket
from mainapp.models import Product


@login_required
def basket_view(request):
    title = 'basket'
    basket_items = Basket.objects.filter(user=request.user). \
        order_by('product__category')

    my_context = {
        'title': title,
        'basket_items': basket_items,
    }

    return render(request, 'basketapp/basket.html', my_context)


@login_required
def basket_add_view(request, pk):
    if 'login' in request.META.get('HTTP_REFERER'):
        return HttpResponseRedirect(reverse('products:product', args=[pk]))

    product = get_object_or_404(Product, pk=pk)
    basket = Basket.objects.filter(user=request.user, product=product).first()

    if not basket:
        basket = Basket(user=request.user, product=product)

    basket.quantity += 1
    basket.save()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required
def basket_remove_view(request, pk):
    basket_record = get_object_or_404(Basket, pk=pk)
    basket_record.delete()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required
def basket_update_view(request, pk, quantity):
    print('ajax works')
    if request.is_ajax():
        basket_item = get_object_or_404(Basket, pk=int(pk))
        quantity = int(quantity)
        if quantity > 0:
            basket_item.quantity = quantity
            basket_item.save()
        else:
            basket_item.delete()

        my_context = {
            'basket_items': request.user.basket.all().order_by('product__category'),
        }
        result = render_to_string('basketapp/includes/inc_basket_list.html', my_context)

        return JsonResponse({
            'result': result
        })
