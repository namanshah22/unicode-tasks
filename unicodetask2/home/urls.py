from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("",views.index, name='home'),
    path("checkbits/",views.checkbits),
    path("checkbits/<int:a>/<int:b>/",views.index)
]