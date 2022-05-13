from django.contrib import admin
from .models import Topping, Pizza, PizzaTopping

class PizzaToppingInline(admin.TabularInline):
    model = PizzaTopping

class PizzaAdmin(admin.ModelAdmin):
    inlines = [PizzaToppingInline,]

class ToppingAdmin(admin.ModelAdmin):
    inlines = [PizzaToppingInline,]

admin.site.register(Pizza, PizzaAdmin)
admin.site.register(Topping, ToppingAdmin)