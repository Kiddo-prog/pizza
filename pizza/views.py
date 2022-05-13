from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from .models import Pizza, PizzaTopping, Topping
from cart.forms import CartAddPizzaForm

# @login_required
def dashboard(request):
    return render(request, 'dashboard/dashboard.html', {})


class ListPizza(ListView):
    model = PizzaTopping
    template = 'pizza/pizzatopping_list.html'
    context_object_name = 'pizza'

def pizza_detail(request, slug):
    pizza = get_object_or_404(PizzaTopping, slug=slug)
    cart_form = CartAddPizzaForm()
    return render(request, 'pizza/detail.html', {'cart_form': cart_form, 'pizza': pizza})
