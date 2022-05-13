from decimal import Decimal
from django.conf import settings
from pizza.models import PizzaTopping

class Cart(object):
    #Initialize session for storing cart values
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    # function for storing cart values
    def add(self, pizza, quantity=1, override_quantity=False):
        pizza_id = str(pizza.id)
        if pizza_id not in self.cart:
            self.cart[pizza_id] = {'quantity': 0, 'price': str(pizza.price)}
        if override_quantity:
            self.cart[pizza_id]['quantity'] = quantity
        else:
            self.cart[pizza_id]['quantity'] += quantity
        self.save()

    def save(self):
        self.session.modified = True
    
    def remove(self, pizza):
        pizza_id = str(pizza.id)
        if pizza_id in self.cart:
            del self.cart[pizza_id]
            self.save()

    def __iter__(self):
        pizza_id = self.cart.keys()
        pizzas = PizzaTopping.objects.filter(id__in=pizza_id)

        cart = self.cart.copy()
        for pizza in pizzas:
            cart[str(pizza.id)]['pizza'] = pizza

        for item in cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item
    # Get length of items in cart
    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())

    def get_total_price(self):
        return sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values())

    def clear(self):
        del self.session[settings.CART_SESSION_ID]
        self.save()
