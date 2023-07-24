
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include("class.urls")),
    path('stream/',include('streams.urls'))
]
