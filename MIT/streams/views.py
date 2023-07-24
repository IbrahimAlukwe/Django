
from django.shortcuts import render

# Create your views here.

def streams(request):
    return render(request, 'stream.html')


