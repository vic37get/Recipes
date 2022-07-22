from django.contrib import admin
from django.urls import path

from recipes.views import contato, home, sobre

urlpatterns = [
    path('', home),  # home
    path('sobre/', sobre),  # sobre
    path('contato/', contato),  # contato
]
