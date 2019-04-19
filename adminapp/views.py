from django.contrib.auth.mixins import UserPassesTestMixin
from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import user_passes_test
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
#from django.utils.decorators import method_decorator

from authapp.models import ShopUser
from mainapp.models import ProductCategory, Product

from authapp.forms import ShopUserRegisterForm
from adminapp.forms import ShopUserAdminEditForm


# user views


class IsSuperUserView(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_superuser


class ShopUserListView(IsSuperUserView, ListView):
    model = ShopUser
    template_name = 'adminapp/users.html'

    def get_context_data(self, **kwargs):
        my_context = super(ShopUserListView, self).get_context_data(**kwargs)
        my_context['title'] = 'Users list'
        return my_context


class ShopUserCreateView(IsSuperUserView, CreateView):
    model = ShopUser
    template_name = 'adminapp/user_update.html'
    fields = '__all__'
    success_url = reverse_lazy('admin_custom:users')

    def get_context_data(self, **kwargs):
        my_context = super(ShopUserCreateView, self).get_context_data(**kwargs)
        my_context['title'] = 'User create'
        return my_context


class ShopUserUpdateView(IsSuperUserView, UpdateView):
    model = ShopUser
    template_name = 'adminapp/user_update.html'
    fields = '__all__'
    success_url = reverse_lazy('admin_custom:users')

    def get_context_data(self, **kwargs):
        my_context = super(ShopUserUpdateView, self).get_context_data(**kwargs)
        my_context['title'] = 'User update'
        return my_context


class ShopUserDeleteView(IsSuperUserView, DeleteView):
    model = ShopUser
    template_name = 'adminapp/user_update.html'
    success_url = reverse_lazy('admin_custom:users')

    def get_context_data(self, **kwargs):
        my_context = super(ShopUserDeleteView, self).get_context_data(**kwargs)
        my_context['title'] = 'User delete'
        return my_context

    def delete(self, request, *args, **kwargs):
        user = get_object_or_404(ShopUser, pk=kwargs['pk'])
        user.is_active = False
        user.save()
        return HttpResponseRedirect(self.success_url)


# category views


class ProductCategoryListView(IsSuperUserView, ListView):
    model = ProductCategory
    template_name = 'adminapp/categories.html'

    def get_context_data(self, **kwargs):
        my_context = super(ProductCategoryListView, self).get_context_data(**kwargs)
        my_context['title'] = ' Categories List'
        return my_context

    #@method_decorator(user_passes_test(lambda u: u.is_superuser))
    #def dispatch(self, *args, **kwargs):
    #    return super(ProductCategoryListView, self).dispatch(*args, **kwargs)


class ProductCategoryCreateView(IsSuperUserView, CreateView):
    model = ProductCategory
    template_name = 'adminapp/category_update.html'
    success_url = reverse_lazy('admin_custom:categories')
    fields = '__all__'

    def get_context_data(self, **kwargs):
        my_context = super(ProductCategoryCreateView, self).get_context_data(**kwargs)
        my_context['title'] = 'Create category'
        return my_context


class ProductCategoryUpdateView(IsSuperUserView, UpdateView):
    model = ProductCategory
    template_name = 'adminapp/category_update.html'
    success_url = reverse_lazy('admin_custom:categories')
    fields = '__all__'

    def get_context_data(self, **kwargs):
        my_context = super(ProductCategoryUpdateView, self).get_context_data(**kwargs)
        my_context['title'] = 'Update category'
        return my_context


class ProductCategoryDeleteView(IsSuperUserView, DeleteView):
    model = ProductCategory
    template_name = 'adminapp/category_update.html'
    success_url = reverse_lazy('admin_custom:categories')

    def get_context_data(self, **kwargs):
        my_context = super(ProductCategoryDeleteView, self).get_context_data(**kwargs)
        my_context['title'] = 'Delete category'
        return my_context


# product views


@user_passes_test(lambda u: u.is_superuser)
def products_view(request, pk):
    title = 'админка/продукт'

    category = get_object_or_404(ProductCategory, pk=pk)
    products_list = Product.objects.filter(category__pk=pk).order_by('name')

    my_context = {
        'title': title,
        'category': category,
        'objects': products_list,
    }

    return render(request, 'adminapp/products.html', my_context)


@user_passes_test(lambda u: u.is_superuser)
def product_create_view(request, pk):
    pass


@user_passes_test(lambda u: u.is_superuser)
def product_read_view(request, pk):
    pass


@user_passes_test(lambda u: u.is_superuser)
def product_update_view(request, pk):
    pass


@user_passes_test(lambda u: u.is_superuser)
def product_delete_view(request, pk):
    pass
