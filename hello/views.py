from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render (request, 'hello/index.html')


def greeting(request, name):
    return render (request,'hello/greeting.html',{
        'name': name.capitalize(),
        'var': 'Tested Text'
    })