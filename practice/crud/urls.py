
from django.urls import path
from . import views



urlpatterns = [
    path('myyy/',views.myyy, name="myyy")

]