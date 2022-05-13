from timeit import repeat
from xml.dom import ValidationErr
from django.contrib.auth.models import User
from django import forms

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password1 = forms.CharField(label='Repeat Password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'email',)

    def clean_password2(self):
        cd = self.cleaned_data()
        if cd['password'] != cd['password1']:
            return forms.ValidationError('Password Mismatch')
        return cd['password2']
