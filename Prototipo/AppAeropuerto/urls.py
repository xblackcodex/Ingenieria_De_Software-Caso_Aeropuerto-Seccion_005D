from unicodedata import name
from django.urls import path 
from .views import inicio, mostrar

urlpatterns = [ 
    path('',inicio,name="inicio"),
    path('mostrar/',mostrar,name="mostrar"),
] 