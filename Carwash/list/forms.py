from datetime import datetime
from .models import Registration, Booking
from django.forms import ModelForm, TextInput, PasswordInput, EmailInput, TimeInput, DateInput, SelectMultiple
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

        widgets = {
            'username': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ваш никнейм',
                'style': 'padding-right: 20px; background-color: rgb(251, 202, 1); display: block; width: 300px;'
                         'font-size: 15px; text-align: left;  margin-bottom: 20px; margin-top: 10px;'
            }),
            'email': EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ваш email',
                'style': 'padding-right: 20px; background-color: rgb(251, 202, 1); display: block; width: 300px;'
                         'font-size: 15px; text-align: left; margin-bottom: 20px; margin-top: 10px;'
            }),
            'password1': PasswordInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ваш пароль',
            }),
            'password2': PasswordInput(attrs={
                'class': 'form-control',
                'placeholder': 'Повторите пароль',

            }),

        }


class BookingForm(ModelForm):
    class Meta:
        model = Booking
        fields = ['name', 'column_number', 'car_number', 'time']
        widgets = {
            'name': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Напишите ваше Имя'
            }),
            'column_number': TextInput(attrs={
                'class': 'form-control',
                'placeholder': '1, 2, 3 или 4'

            }),
            'car_number': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Напишите номер машины'
            }),
            'time': TextInput(attrs={
                'class': 'form-control',
                'placeholder': datetime.now().strftime("%H:%M")
            })
        }
