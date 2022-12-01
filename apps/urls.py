from django.urls import path
from .views import *


urlpatterns = [
    path('', index, name='home'),
    path('login/', login, name='login'),
    path('cadastre/', cadastre, name='cadastre'),
    path('produtos/', produtos, name='produtos')
]
a
