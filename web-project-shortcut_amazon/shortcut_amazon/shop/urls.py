
from django.urls.conf import include
from .views import cart, home
from django.urls import path
urlpatterns = [
  path('',home,name='main'),
  path('home/cart',cart,name='shopping'),
]
