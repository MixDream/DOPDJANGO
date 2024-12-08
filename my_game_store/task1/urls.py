from django.urls import path
from .views import index, games_list, cart, registration

urlpatterns = [
    path('', index, name='index'),
    path('games/', games_list, name='games_list'),
    path('cart/', cart, name='cart'),
    path('registration/', registration, name='registration'),
]
from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_posts, name='create_posts'),
    path('update/<int:post_id>/', views.update_post, name='update_post'),
    path('list/', views.list_posts, name='list_posts'),
    path('delete/<int:post_id>/', views.delete_post, name='delete_post'),
    path('filter/', views.filter_posts, name='filter_posts'),
]
