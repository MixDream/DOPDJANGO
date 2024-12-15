from django.urls import path
import views

urlpatterns = [
    path('', views.index, name='index'),
    path('games/', views.games_list, name='games_list'),
    path('cart/', views.cart, name='cart'),
    path('registration/', views.registration, name='registration'),
    # Добавьте дополнительные пути для других представлений
    path('create/', views.create_posts, name='create_posts'),
    path('update/<int:post_id>/', views.update_post, name='update_post'),
    path('list/', views.list_posts, name='list_posts'),
    path('delete/<int:post_id>/', views.delete_post, name='delete_post'),
    path('filter/', views.filter_posts, name='filter_posts'),
]
