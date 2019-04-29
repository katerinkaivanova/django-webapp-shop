from django.contrib.auth.mixins import UserPassesTestMixin
from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import user_passes_test
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.utils.decorators import method_decorator

from authapp.models import ShopUser
from mainapp.models import ProductCategory, Product

from authapp.forms import ShopUserRegisterForm
from adminapp.forms import ShopUserAdminEditForm


# user views


class IsSuperUserMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_superuser


class ShopUserListView(IsSuperUserMixin, ListView):
    model = ShopUser
    template_name = 'adminapp/users.html'

    def get_context_data(self, **kwargs):
        my_context = super(ShopUserListView, self).get_context_data(**kwargs)
        my_context['title'] = 'Users list'

        return my_context


class ShopUserCreateView(IsSuperUserMixin, CreateView):
    model = ShopUser
    template_name = 'adminapp/user_update.html'
    fields = '__all__'
    success_url = reverse_lazy('admin_custom:users')

    def get_context_data(self, **kwargs):
        my_context = super(ShopUserCreateView, self).get_context_data(**kwargs)
        my_context['title'] = 'User create'

        return my_context


class ShopUserUpdateView(IsSuperUserMixin, UpdateView):
    model = ShopUser
    template_name = 'adminapp/user_update.html'
    fields = '__all__'
    success_url = reverse_lazy('admin_custom:users')

    def get_context_data(self, **kwargs):
        my_context = super(ShopUserUpdateView, self).get_context_data(**kwargs)
        my_context['title'] = 'User update'

        return my_context


class ShopUserDeleteView(IsSuperUserMixin, DeleteView):
    model = ShopUser
    template_name = 'adminapp/user_delete.html'
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


class ProductCategoryListView(IsSuperUserMixin, ListView):
    model = ProductCategory
    template_name = 'adminapp/categories.html'

    def get_context_data(self, **kwargs):
        my_context = super(ProductCategoryListView, self).get_context_data(**kwargs)
        my_context['title'] = ' Categories List'

        return my_context


class ProductCategoryCreateView(IsSuperUserMixin, CreateView):
    model = ProductCategory
    template_name = 'adminapp/category_update.html'
    success_url = reverse_lazy('admin_custom:categories')
    fields = '__all__'

    def get_context_data(self, **kwargs):
        my_context = super(ProductCategoryCreateView, self).get_context_data(**kwargs)
        my_context['title'] = 'Create category'

        return my_context


class ProductCategoryUpdateView(IsSuperUserMixin, UpdateView):
    model = ProductCategory
    template_name = 'adminapp/category_update.html'
    success_url = reverse_lazy('admin_custom:categories')
    fields = '__all__'

    def get_context_data(self, **kwargs):
        my_context = super(ProductCategoryUpdateView, self).get_context_data(**kwargs)
        my_context['title'] = 'Update category'

        return my_context


class ProductCategoryDeleteView(IsSuperUserMixin, DeleteView):
    model = ProductCategory
    template_name = 'adminapp/category_delete.html'
    success_url = reverse_lazy('admin_custom:categories')

    def get_context_data(self, **kwargs):
        my_context = super(ProductCategoryDeleteView, self).get_context_data(**kwargs)
        my_context['title'] = 'Delete category'

        return my_context

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.is_active = False
        self.object.save()

        return HttpResponseRedirect(self.get_success_url())


# product views


class ProductListView(IsSuperUserMixin, ListView):
    model = Product
    template_name = 'adminapp/products.html'

    def get_context_data(self, **kwargs):
        my_context = super(ProductListView, self).get_context_data(**kwargs)
        my_context['category'] = self.kwargs['pk']
        my_context['name'] = ProductCategory.objects.get(pk=self.kwargs['pk'])
        my_context['title'] = 'Products list'

        return my_context

    def get_queryset(self, *args, **kwargs):
        queryset = Product.objects.filter(category__pk=self.kwargs['pk'])

        return queryset


class ProductReadView(IsSuperUserMixin, DetailView):
    model = Product
    template_name = 'adminapp/product_read.html'
    success_url = reverse_lazy('adminapp:products')


    def get_context_data(self, **kwargs):
        my_context = super(ProductReadView, self).get_context_data(**kwargs)
        my_context['title'] = 'Product details'

        return my_context


class ProductCreateView(IsSuperUserMixin, CreateView):
    model = Product
    template_name = 'adminapp/category_update.html'
    fields = '__all__'
    success_url = reverse_lazy('admin_custom:categories')


class ProductUpdateView(IsSuperUserMixin, UpdateView):
    model = Product
    fields = '__all__'
    template_name = 'adminapp/product_update.html'

    def get_success_url(self):

        return reverse_lazy('adminapp:product_update', kwargs={'pk': self.kwargs.get('pk')})

    def get_context_data(self, **kwargs):
        my_context = super(ProductUpdateView, self).get_context_data(**kwargs)
        my_context['title'] = f"Edit product {my_context.get('object').name}"

        return my_context


class ProductDeleteView(IsSuperUserMixin, DeleteView):
    model = Product
    template_name = 'adminapp/product_delete.html'
    success_url = reverse_lazy('adminapp:categories')

    def get_context_data(self, **kwargs):
        my_context = super(ProductDeleteView, self).get_context_data(**kwargs)
        my_context['title'] = f"Delete product {my_context.get('object').name}"

        return my_context

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.is_active = False
        self.object.save()

        return HttpResponseRedirect(self.get_success_url())
