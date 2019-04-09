from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from django.contrib import auth
from authapp.forms import ShopUserRegisterForm, ShopUserEditForm, ShopUserLoginForm


def register_view(request):
    title = 'register'

    if request.method == 'POST':
        register_form = ShopUserRegisterForm(request.POST, request.FILES)

        if register_form.is_valid():
            new_user = register_form.save()
            auth.login(request, new_user)
            return HttpResponseRedirect(reverse('main'))
    else:
        register_form = ShopUserRegisterForm()

    my_context = {'title': title, 'register_form': register_form}
    return render(request, 'authapp/register.html', my_context)


def edit_view(request):
    title = 'edit'

    if request.method == 'POST':
        edit_form = ShopUserEditForm(request.POST, request.FILES, instance=request.user)
        if edit_form.is_valid():
            edit_form.save()
            return HttpResponseRedirect(reverse('auth:edit'))
    else:
        edit_form = ShopUserEditForm(instance=request.user)

    context = {'title': title, 'edit_form': edit_form}

    return render(request, 'authapp/edit.html', context)


def login_view(request):
    title = 'sign in'

    login_form = ShopUserLoginForm(data=request.POST)
    if request.method == 'POST' and login_form.is_valid():
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user and user.is_active:
            auth.login(request, user)
            return HttpResponseRedirect(reverse('main'))

    my_context = {'title': title, 'login_form': login_form}
    return render(request, 'authapp/login.html', my_context)


def logout_view(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('main'))
