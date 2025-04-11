from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import Product
from .forms import ProductForm, RegisterForm



def register_view(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()  
            login(request, user)  
            return redirect('product-list') 
        messages.error(request, 'There was an error in your registration.')
    return render(request, 'invApp/register_login.html', {'form': form, 'page': 'register'})


def login_view(request):
    page = 'login'
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  
        messages.error(request, 'Username or password is incorrect.')
    return render(request, 'invApp/register_login.html', {'page': page})


def logout_view(request):
    logout(request)
    return redirect('home') 


def home_view(request):
    return render(request, 'invApp/home.html')


@login_required(login_url='login')
def product_create_view(request):
    form = ProductForm()
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            product = form.save(commit=False)  
            product.user = request.user  
            product.save()  
            messages.success(request, 'Product added successfully.')
            return redirect('product-list')
    return render(request, 'invApp/product_form.html', {'form': form})


@login_required(login_url='login')
def product_list_view(request):
    products = Product.objects.filter(user=request.user)  
    return render(request, 'invApp/product_list.html', {'products': products})


@login_required(login_url='login')
def product_update_view(request, pk):
    product = Product.objects.get(id=pk)
    form = ProductForm(instance=product)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Product updated successfully.')
            return redirect('product-list')
    return render(request, 'invApp/product_form.html', {'form': form})


@login_required(login_url='login')
def product_delete_view(request, pk):
    product = Product.objects.get(id=pk)
    if request.method == 'POST':
        product.delete()
        messages.success(request, 'Product deleted successfully.')
        return redirect('product-list')
    return render(request, 'invApp/product_confirm_delete.html', {'product': product})
