import datetime
from django.shortcuts import render

def index(request):
    dt = datetime.datetime.now()
    return render(request, 'newyear/index.html',{
        'newyear': dt.day == 1 and dt.month == 1
    })
