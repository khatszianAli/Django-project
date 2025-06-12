from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.urls import reverse_lazy
from django.views.generic import FormView
from django.contrib import messages
from datetime import datetime, timedelta
from django.views.generic import DetailView, UpdateView, DeleteView, TemplateView
from .models import Registration, Booking
from .forms import RegistrationForm, BookingForm
from django import template

register = template.Library()


@register.filter
def capfirst(value):
    if isinstance(value, str) and value:
        return value[0].upper() + value[1:]
    return value


def lists(request):
    return render(request, 'list/list.html')


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            login(request, form.save())
            return redirect('list')
    else:
        form = RegistrationForm()
    return render(request, 'list/register.html', {"form": form})


def userlogin(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('list')
    else:
        form = AuthenticationForm()
    return render(request, 'list/login.html', {"form": form})


def userloginout(request):
    logout(request)
    return render(request, 'list/list.html')


def mark(request):
    bookings = Booking.objects.all()
    date = datetime.today().date()
    time = datetime.strptime(datetime.now().strftime("%H:%M"), "%H:%M")
    start_time = datetime.strptime("10:00", "%H:%M")
    end_time = datetime.strptime("21:00", "%H:%M")

    user = request.user
    if user.is_authenticated:
        if request.method == "POST":
            form = BookingForm(request.POST)
            if form.is_valid():
                booking = form.save(commit=False)
                booking.user = request.user  # Associate the booking with the logged-in user
                booking.save()
                # form.save()
                return redirect('list')

        else:
            form = BookingForm(request.POST)
        return render(request, 'list/mark.html', {'date': date, 'time': time, 'start_time': start_time,
                                                  'end_time': end_time, 'bookings': bookings, 'form': form})
    else:
        messages.error(request, "Для записи вам нужно будет войти или зарегистрироваться")
        return redirect('list')


def table(request):
    bookings = Booking.objects.all()

    start_time = datetime.strptime("10:00", "%H:%M")
    end_time = datetime.strptime("21:00", "%H:%M")
    increment = timedelta(minutes=20)

    time_slots = []
    booking_slots = {'1': [], '2': [], '3': [], '4': []}
    current_time = start_time
    while current_time <= end_time:
        time_slots.append(current_time.strftime("%H:%M"))
        current_time += increment

    for i in bookings:
        booking_slots[i.column_number].append(i.time.strftime("%H:%M"))

    if datetime.now().time().strftime("%H:%M") > end_time.time().strftime("%H:%M"):
        var = Booking.objects.all()
        var.delete()
    date = datetime.today().date()
    return render(request, 'list/table.html', {
        'dates': date,
        'slots': time_slots,
        'booking_slots': booking_slots,
        'bookings': bookings
    })


class Detail(TemplateView):
    template_name = 'list/detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        slot = kwargs.get('slot')
        context['slot'] = slot
        bookings = Booking.objects.filter(time=slot)
        if bookings.exists():
            context['bookings'] = bookings
        else:
            context['bookings'] = None
        return context


class BookingDeleteView(DeleteView):
    model = Booking
    template_name = 'list/booking_delete.html'  # Template to confirm deletion
    context_object_name = 'booking'
    success_url = reverse_lazy('list')  # Redirect to the booking list after deletion

    def get_object(self, queryset=None):
        # Get the booking object based on the slot
        slot = self.kwargs.get('slot')
        booking = Booking.objects.filter(time=slot).first()
        return booking
