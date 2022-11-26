from django.urls import path
from .views import *


urlpatterns = [
    path('', index),
    path('login/', login),
    path('cadastre/', cadastre),
    path('produtos/', produtos)
]

