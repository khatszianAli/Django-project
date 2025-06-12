from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.db import models
from django import forms


# Create your models here.


class Registration(UserCreationForm):
    user = models.CharField('Напишите ваше Имя', max_length=25)
    email = models.EmailField('Напишите вашу почту', unique=True)
    password1 = models.CharField('Придумайте пароль', max_length=120)
    password2 = models.CharField('Повторите пароль', max_length=120)

    def __str__(self):
        return self.user


class Booking(models.Model):
    name = models.CharField('Напишите ваше Имя', max_length=25)
    column_number = models.CharField('Напишите номер колоны c 1-ой по 4-ую', max_length=25)
    car_number = models.CharField('Напишите номер машины', max_length=25)
    time = models.TimeField('Напишите время брони')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bookings', verbose_name='Пользователь',  null=True, blank=True)

    def __str__(self):
        return f"{self.name} ({self.user.username})"
