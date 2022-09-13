from django.shortcuts import render, get_object_or_404, redirect

from .cart import Cart
from .forms import AddToCartProductForm
from products.models import Product

# Create your views here.

def cart_detail_view(request):
    cart = Cart(request)
    return render(request, 'cart/cart_detail.html', context={'cart': cart})

def add_to_cart_view(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = AddToCartProductForm(request.POST)
    if form.is_valid():
        cleaned_data = form.cleaned_data
        quantity = cleaned_data['quantity']
        cart.add(product, quantity)
        # print(f"form: {form}")
        # print(f"cleaned data: {cleaned_data}")
        # print(f"quantity: {quantity}")

    return redirect('cart:cart_detail')


