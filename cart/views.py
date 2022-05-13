from django.shortcuts import render, redirect, get_object_or_404
from .forms import CartAddPizzaForm
from pizza.models import PizzaTopping
from .cart import Cart
from django.views.decorators.http import require_POST


@require_POST
def cart_add(request, pizza_id):
    cart = Cart(request)
    pizza = get_object_or_404(PizzaTopping, id=pizza_id)
    form = CartAddPizzaForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(pizza=pizza, quantity=cd['quantity'], override_quantity=cd['override'])    
    return redirect('cart:detail')


@require_POST
def cart_remove(request, pizza_id):
    cart = Cart(request)
    pizza = get_object_or_404(PizzaTopping, id=pizza_id)
    cart.remove(pizza)
    return redirect('pizza:list')

def cart_detail(request):
    cart = Cart(request)
    return render(request, 'cart/detail.html', {'cart': cart})