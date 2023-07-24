



from django.contrib import admin
from django.urls import path

from . import views


urlpatterns = [
    path('',views.index.html, name='index.html'),
    path('inner-page/',views.inner.html, name='inner-page.html'),
    path('portfolio-details/',views.portfolio.html, name='portfolio-details.html'),
    path('readme/', views.Readme.html, name='readme.html')
]
