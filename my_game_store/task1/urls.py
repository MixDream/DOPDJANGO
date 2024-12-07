from django.urls import path
from .views import index, games_list, cart, registration

urlpatterns = [
    path('', index, name='index'),
    path('games/', games_list, name='games_list'),
    path('cart/', cart, name='cart'),
    path('registration/', registration, name='registration'),
]
