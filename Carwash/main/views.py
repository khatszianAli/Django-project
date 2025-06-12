from datetime import datetime

from django.shortcuts import render


# Create your views here.


def home(request):
    time = datetime.strptime(datetime.now().strftime("%H:%M"), "%H:%M")
    start_time = datetime.strptime("10:00", "%H:%M")
    end_time = datetime.strptime("21:00", "%H:%M")
    return render(request, 'main/index.html', {'time': time, 'start_time': start_time,
                                               'end_time': end_time})
