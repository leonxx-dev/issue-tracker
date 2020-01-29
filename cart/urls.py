from django.urls import path, re_path
from .views import view_cart, add_to_cart, remove_from_cart

urlpatterns = [
    path('', view_cart, name='view_cart'),
    re_path(r'^add/(?P<id>\d+)', add_to_cart, name='add_to_cart'),
    re_path(r'^remove/(?P<id>\d+)', remove_from_cart, name='remove_from_cart'),
]