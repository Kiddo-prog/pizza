from django.shortcuts import render, get_object_or_404, redirect
from .models import OrderItem
from .forms import OrderForm
from .forms import OrderForm
from cart.cart import Cart

def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid:
            order = form.save()
            for item in cart:
                OrderItem.objects.create(order=order, pizza=item['pizza'], price=item['price'], quantity=item['quantity'])
            cart.clear()
            return render(request, 'order/created.html', {'order': order})

    else:
        form = OrderForm()
    return render(request, 'order/create.html', {'form': form, 'cart': cart})            