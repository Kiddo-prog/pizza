from django import forms

PIZZA_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 21)]

class CartAddPizzaForm(forms.Form):
    quantity = forms.TypedChoiceField(choices=PIZZA_QUANTITY_CHOICES, coerce=int)
    override = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)

    