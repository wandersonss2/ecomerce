from django.urls import path
from .views import *


urlpatterns = [
    path('', index, name='home'),
    path('cadastre/', cadastre, name='cadastre'),
    path('produtos/', produtos, name='produtos'),
    path('carrinho/', carrinho, name='carrinho')
]

