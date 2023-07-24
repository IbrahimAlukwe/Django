from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.


def home(request):
    return render(request,'home.html')

def About(request):
    return render(request,'About.html')

def contact(request):
    return render(request, 'contacts.html')


def contacts(request):
    return render(request,'contacts.html')