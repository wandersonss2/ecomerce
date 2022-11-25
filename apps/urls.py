from django.urls import path
from .views import *


urlpatterns = [
    path('', index),
    path('login/', login),
    path('sobre/', cadastre),
    path('produtos/', produtos)
]

