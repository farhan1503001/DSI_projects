
from django.urls.conf import include
from .views import cart, home
from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns = [
  path('',home,name='main'),
  path('home/cart',cart,name='shopping'),
]

urlpatterns+=staticfiles_urlpatterns()