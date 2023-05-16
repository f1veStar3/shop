from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms


from .models import *


class OrderForm(forms.ModelForm):

    class Meta:
        model = Order
        fields = (
            'first_name', 'last_name', 'phone', 'buying_type', 'state', 'number_nova_post', 'comment', 'payment_method',
        )

class RegisterUserForm(UserCreationForm):
    username = forms.EmailField(label='Email')
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput())
    password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')


class LoginUserForm(AuthenticationForm):

    username = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Пароль'}))

    error_messages = {
        'invalid_login': "Неправильний логін або пароль",
        'inactive': "Цей аккаунт неактивний",
    }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


