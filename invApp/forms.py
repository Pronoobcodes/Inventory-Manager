from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Product

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'sku', 'price', 'quantity', 'supplier']  
        labels = {
            'name': 'Product Name',
            'sku': 'SKU',
            'price': 'Price',
            'quantity': 'Quantity',
            'supplier': 'Supplier',
        }
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'e.g shirt', 'class': 'form-control'}),
            'sku': forms.TextInput(attrs={'placeholder': 'e.g S1234', 'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'placeholder': 'e.g 19.99', 'class': 'form-control'}),
            'quantity': forms.NumberInput(attrs={'placeholder': 'e.g 10', 'class': 'form-control'}),
            'supplier': forms.TextInput(attrs={'placeholder': 'e.g Nintendo', 'class': 'form-control'}),
        }
