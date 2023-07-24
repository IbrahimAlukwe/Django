
from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'index.html')


def mm(request):
    return render(request, 'mm.html')

def insertdata(request):
    return render(request, 'mm.html')