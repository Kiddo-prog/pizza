from operator import imod
from django import forms
from .models import Pizza, Topping

class PizzaForm(forms.ModelForm):
    class Meta:
        model = Pizza
        fields = '__all__'

class ToppingForm(forms.ModelForm):
    class Meta:
        model = Topping
        fields = '__all__'